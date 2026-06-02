import numbers.Rational
import figures._

// scala run -M Solution .
object Solution extends App:
    val r1 = Rational(6, 7)
    val r2 = Rational(6, 9)

    println(s"r1 = $r1")
    println(s"r2 = $r2")
    println(s"r1 + r2 = ${r1 + r2}")
    println(s"r1 - r2 = ${r1 - r2}")
    println(s"r1 * r2 = ${r1 * r2}")
    println(s"r1 / r2 = ${r1 / r2}")

    val rZero = Rational.zero
    val rOne = Rational.one
    val rTwo = Rational(2)

    try { Rational(1, 0) } catch {
        case e: IllegalArgumentException =>
            println(s"${e.getMessage}")
    }

    val triangle = Triangle((0,0), (4,0), (0,3))
    println(s"${triangle.description} area = ${triangle.area}")

    try { val invalidTriangle = Triangle((0,0),(1,1),(2,2)) } catch {
        case e: IllegalArgumentException =>
            println(s"${e.getMessage}")
    }

    val rectangle = Rectangle.fromPoint(1, 1, 5, 2)
    println(s"${rectangle.description} area = ${rectangle.area}")

    try { val invalidRectangle = new Rectangle(Point(0, 0), Point(1, 0), Point(2, 1), Point(0, 1)) } catch {
        case e: IllegalArgumentException =>
            println(s"${e.getMessage}")
    }

    val square = Square.fromPoint(0, 0, 3)
    println(s"${square.description} area = ${square.area}")

    try { val invalidSquare = new Square(Point(0, 0), Point(2, 0), Point(2, 3), Point(0, 3)) } catch {
        case e: IllegalArgumentException =>
            println(s"${e.getMessage}")
    }

    val figuresList: List[Figure] =
        List(triangle, rectangle, square)

    println("\nArea of all figures: " + FigureUtils.areaSum(figuresList))

    FigureUtils.printAll(figuresList)