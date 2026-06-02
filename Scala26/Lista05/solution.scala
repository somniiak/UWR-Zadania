package plugins:
    trait Pluginable:
        def apply(text: String): Option[String] = Option(text)

        def unwrap(textOpt: Option[String]): String =
            textOpt match
                case Some(text) => text
                case None => ""

    trait Reverting extends Pluginable:
        override def apply(text: String): Option[String] =
            super.apply(text).map(_.reverse)

    trait LowerCasing extends Pluginable:
        override def apply(text: String): Option[String] =
            super.apply(text).map(_.toLowerCase)

    trait SingleSpacing extends Pluginable:
        override def apply(text: String): Option[String] =
            super.apply(text).map(_.replaceAll(" +", " "))

    trait NoSpacing extends Pluginable:
        override def apply(text: String): Option[String] =
            super.apply(text).map(_.replaceAll(" +", ""))

    trait DuplicateRemoval extends Pluginable:
        override def apply(text: String): Option[String] =
            super.apply(text).map(s => s.filter(c => (s.count(_ == c) == 1)))

    trait Rotating extends Pluginable:
        override def apply(text: String): Option[String] =
            super.apply(text).flatMap(s =>
                if s.isEmpty then None
                else Some(s.last.toString + s.init)
            )

    trait Doubling extends Pluginable:
        override def apply(text: String): Option[String] =
            super.apply(text).map(_.zipWithIndex
                .foldLeft("")((acc, ci) => {
                    if ci._2 % 2 == 0 then acc :+ ci._1
                    else acc :+ ci._1 :+ ci._1
                }))

    trait Shortening extends Pluginable:
        override def apply(text: String): Option[String] =
            super.apply(text).map(_.zipWithIndex
                .foldLeft("")((acc, ci) => {
                    if ci._2 % 2 == 0 then acc :+ ci._1
                    else acc
                }))

object Actions:
    import plugins._

    // SingleSpacing => Doubling => Shortening
    val actionA: Pluginable = new Pluginable with SingleSpacing with Doubling with Shortening

    // NoSpacing => Shortening => Doubling
    val actionB: Pluginable = new Pluginable with NoSpacing with Shortening with Doubling

    // LowerCasing => Doubling
    val actionC: Pluginable = new Pluginable with LowerCasing with Doubling

    // DuplicateRemoval => Rotating
    val actionD: Pluginable = new Pluginable with DuplicateRemoval with Rotating

    // NoSpacing => Shortening => Doubling => Reverting
    val actionE: Pluginable = new Pluginable with NoSpacing with Shortening with Doubling with Reverting

    // Rotating 5-times
    val actionF: Pluginable = new Pluginable with Rotating:
        override def apply(text: String): Option[String] =
            (1 to 5).foldLeft(Option(text))((acc, _) => acc.flatMap(super.apply))

    // actionA => actionB
    val actionG: Pluginable = new Pluginable:
        override def apply(text: String): Option[String] =
            actionA.apply(text).flatMap(actionB.apply)

@main def main(): Unit =
    import Actions._
    import plugins._

    def test(name: String, action: Pluginable, input: String): Unit =
        val result = action.unwrap(action(input))
        println(s"$name('$input') => '$result'")

    val tests = List(
        "Hello World",
        "  Hello  World  ",
        "aabbcc",
        "Hello",
        "",
    )

    tests.foreach(test("actionA", actionA, _))
    tests.foreach(test("actionB", actionB, _))
    tests.foreach(test("actionC", actionC, _))
    tests.foreach(test("actionD", actionD, _))
    tests.foreach(test("actionE", actionE, _))
    tests.foreach(test("actionF", actionF, _))
    tests.foreach(test("actionG", actionG, _))
