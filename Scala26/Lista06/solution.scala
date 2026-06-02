package pizzeria:
    enum PizzaType(val price: Double):
        case Margarita extends PizzaType(5)
        case Pepperoni extends PizzaType(6.5)
        case Funghi extends PizzaType(7)

    enum Topping(val price: Double):
        case Ketchup extends Topping(0.5)
        case Garlic extends Topping(0.5)

    enum Meat(val price: Double):
        case Salami extends Meat(1)

    enum Drink(val price: Double):
        case Lemonade extends Drink(2)

    enum Size:
        case Small, Regular, Large

    enum Crust:
        case Thin, Thick

    enum Discount:
        case Student, Senior

    case class Pizza(
        pizzaType: PizzaType,
        size: Size,
        crust: Crust,
        extraMeat: Option[Meat] = None,
        extraTopping: Option[Topping] = None
    ):
        override def toString() =
            val meatStr = extraMeat.map(m => s" + $m").getOrElse("")
            val toppingStr = extraTopping.map(t => s" + $t").getOrElse("")
            s"${pizzaType} [${size}, ${crust} crust${meatStr}${toppingStr}] - $$${price}"

        val price: Double =
            val base = pizzaType.price
            val meatExtra = extraMeat.map(_.price).getOrElse(0.0)
            val topExtra = extraTopping.map(_.price).getOrElse(0.0)
            val subtotal = base + meatExtra + topExtra

            size match
                case Size.Small => 0.9 * subtotal
                case Size.Regular => 1 * subtotal
                case Size.Large => 1.5 * subtotal

package orders:
    import pizzeria._

    class Order(
        name: String,
        address: String,
        phone: String,
        pizzas: List[Pizza],
        drinks: List[Drink] = List.empty,
        discount: Option[Discount] = None,
        specialInfo: Option[String] = None
    ):
        require(
            phone.matches("""^(?:\+\d{1,2} ?)?\d{9}$"""),
            s"Invalid phone number: '$phone'"
        )

        override def toString() =
            val pizzaLines = pizzas.map(p => s"  - $p").mkString("\n")
            val drinkLines   = if drinks.isEmpty then "" else "\n" + drinks.map(d => s"  - ${d} - $$${d.price}").mkString("\n")
            val discountLine = discount.map(d => s"\n  Discount : ${d}").getOrElse("")
            val infoLine     = specialInfo.map(i => s"\n  Note     : $i").getOrElse("")

            s"""
            |Name: $name
            |Address: $address
            |Phone: $phone
            |Pizzas:
            |$pizzaLines
            |TOTAL: $$${Math.round(price * 100) / 100.0}
            """.stripMargin

        def extraMeatPrice: Option[Double] =
            val total = pizzas.flatMap(_.extraMeat).map(_.price).sum
            Option.when(total > 0)(total)

        def pizzasPrice: Option[Double] =
            Option.when(pizzas.nonEmpty)(pizzas.map(_.price).sum)

        def drinksPrice: Option[Double] =
            Option.when(drinks.nonEmpty)(drinks.map(_.price).sum)

        def priceByType(pt: PizzaType): Option[Double] =
            val matching = pizzas.filter(_.pizzaType == pt).map(_.price)
            Option.when(matching.nonEmpty)(matching.sum)

        val price: Double =
            val rawPizzas = pizzasPrice.getOrElse(0.0)
            val rawDrinks = drinksPrice.getOrElse(0.0)

            discount match
                case Some(Discount.Student) =>
                    0.95 * rawPizzas + rawDrinks
                case Some(Discount.Senior) =>
                    0.93 * (rawPizzas + rawDrinks)
                case None =>
                    rawPizzas + rawDrinks

@main def run(): Unit =

    import pizzeria._
    import orders._

    val p1 = Pizza(PizzaType.Margarita, Size.Regular, Crust.Thin)
    val p2 = Pizza(PizzaType.Pepperoni, Size.Large,   Crust.Thick, extraMeat = Some(Meat.Salami))
    val p3 = Pizza(PizzaType.Funghi,    Size.Small,   Crust.Thin,  extraTopping = Some(Topping.Garlic))
    val p4 = Pizza(PizzaType.Margarita, Size.Large,   Crust.Thick, extraMeat = Some(Meat.Salami), extraTopping = Some(Topping.Ketchup))
    List(p1, p2, p3, p4).foreach(println)

    val order1 = Order(
        name = "Humbert Humbert",
        address = "Flower Street 42, Beardsley",
        phone = "+1123456789",
        pizzas = List(p1, p2),
        drinks = List(Drink.Lemonade)
    )
    
    println(order1)

    val order2 = Order(
        name = "Mati Batat",
        address = "Nowowiejska 67/4b, Wrocław",
        phone = "+48123456789",
        pizzas = List(p3, p4),
        drinks = List(Drink.Lemonade, Drink.Lemonade),
        discount = Some(Discount.Student),
        specialInfo = Some("Kod do mieszkania 5227.")
    )

    println(order2)