package money:
    import scala.language.implicitConversions

    sealed trait CurrencySymbol
    case object $ extends CurrencySymbol
    case object `€`  extends CurrencySymbol
    case object zl extends CurrencySymbol

    // American dollar as the base of the monetary system
    sealed trait Currency(val symbol: CurrencySymbol, val rateToUSD: BigDecimal)
    case object USD extends Currency($, BigDecimal("1.0000"))
    case object EUR extends Currency(`€`, BigDecimal("1.1797"))
    case object PLN extends Currency(zl, BigDecimal("0.2768"))

    val currencies: List[Currency] = List(USD, EUR, PLN)

    val conversion: Map[(Currency, Currency), BigDecimal] =
        (for
            from <- currencies
            to <- currencies
        yield (from, to) -> (from.rateToUSD / to.rateToUSD)).toMap

    case class CurrencyConverter(conversion: Map[(Currency, Currency), BigDecimal]):
        def convert(from: Currency, to: Currency): BigDecimal =
            conversion(from, to)

    /* ---------------------------------------------------------------------- */

    implicit def symbolToCurrency(symbol: CurrencySymbol): Currency =
        currencies.find(_.symbol == symbol) match
            case Some(currency) => currency
            case None => throw new IllegalArgumentException(s"No currency found for the following symbol: ${symbol}")

    implicit def numberToMoney(amount: Double): Currency => Money =
        (currency: Currency) => Money(amount, currency)(using CurrencyConverter(conversion))

    /* ---------------------------------------------------------------------- */

    case class Money(amount: BigDecimal, currency: Currency)(implicit currencyConverter: CurrencyConverter):
        // https://docs.scala-lang.org/scala3/reference/changed-features/operators.html#the-infix-modifier
        infix def as(currency: Currency): Money =
            new Money(currencyConverter.convert(this.currency, currency) * amount, currency)

        override def toString(): String =
            amount.setScale(2, BigDecimal.RoundingMode.HALF_UP).toString + currency.symbol

        def +(other: Money): Money =
            new Money(amount + (other as currency).amount, currency)

        def -(other: Money): Money =
            new Money(amount - (other as currency).amount, currency)

        def *(multiplier: Double): Money =
            new Money(amount * multiplier, currency)

        def >(other: Money): Boolean =
            amount > (other as currency).amount

        def <(other: Money): Boolean =
            amount < (other as currency).amount

        def ==(other: Money): Boolean =
            amount == (other as currency).amount

        def !=(other: Money): Boolean =
            ! ==(other)

        def >=(other: Money): Boolean =
            ! <(other)

        def <=(other: Money): Boolean =
            ! >(other)

@main def run(): Unit =
    import money._

    val sum1: Money = 100.01(PLN) + 200(EUR)
    val sum2: Money = 100.01(zl) + 200($)
    val sum3: Money = 5(zl) + 3(PLN) + 20.5(USD)
    val sub: Money = 300.01(USD) - 200(EUR)
    val mult1: Money = 30(zl) * 20
    val mult2: Money = 20($) * 11
    val conv1: Money = 150.01(USD) as PLN
    val conv2: Money = 120.01(USD) as `€`
    val compare1: Boolean = 300.30(USD) > 200(`€`)
    val compare2: Boolean = 300.30($) < 200(EUR)

    List(
        sum1,     sum2,     sum3,  sub,
        mult1,    mult2,    conv1, conv2,
        compare1, compare2
    ).foreach(ex => println(ex))