package figures

import numbers.Rational


class Point(_x: Rational, _y: Rational):

    def x = _x

    def y = _y

    def +(other: Point): Point =
        new Point(x + other.x, y + other.y)

    def -(other: Point): Point =
        new Point(x - other.x, y - other.y)

    def +(value: Int): Point =
        new Point(x + Rational(value), y + Rational(value))

    def -(value: Int): Point =
        new Point(x - Rational(value), y - Rational(value))

    def *(value: Int): Point =
        new Point(x * Rational(value), y * Rational(value))

    def /(value: Int): Point =
        new Point(x / Rational(value), y / Rational(value))

    override def toString: String =
        s"($x, $y)"

trait Figure:
    val description: String
    def area: Double

class Triangle(a: Point, b: Point, c: Point) extends Figure:
    require(a != b && b != c && a != c, "Points must be distinct")
    require(Math.abs(((b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y)).toDouble) > 1e-9, "Points must not be collinear")
    override val description: String =
        "Triangle"

    override def area: Double =
        Math.abs((
            (b.x - a.x) * (c.y - a.y) -
            (c.x - a.x) * (b.y - a.y)
        ).toDouble) / 2

class Rectangle(a: Point, b: Point, c: Point, d: Point) extends Figure:
    val sides: List[Double] =
        List(a, b, c, d, a)
        .sliding(2)
        .map({
            case List(fst, snd) => Math.sqrt((
                (fst.x - snd.x) * (fst.x - snd.x) +
                (fst.y - snd.y) * (fst.y - snd.y)
            ).toDouble)
            case _ => 0.0
        })
        .toList

    require(sides(0) == sides(2) && sides(1) == sides(3), "Opposite sides must be equal")

    override val description: String =
        "Rectangle"

    override def area: Double =
        sides.take(2).product

class Square(a: Point, b: Point, c: Point, d: Point) extends Rectangle(a, b, c, d):
    require(sides.distinct.size == 1, "All sides of a square must be equal")
    override val description: String =
        "Square"

object Point:
    def apply(x: Int, y: Int): Point =
        new Point(Rational(x), Rational(y))

    def zero: Point = Point(0, 0)

object Triangle:
    def apply(a: (Int, Int), b: (Int, Int), c: (Int, Int)): Triangle =
        new Triangle(Point(a._1, a._2), Point(b._1, b._2), Point(c._1, c._2))

object Rectangle:
    def fromPoint(x: Int, y: Int, width: Int, height: Int): Rectangle =
        new Rectangle(Point(x, y), Point(x + width, y), Point(x + width, y + height), Point(x, y + height))

    def fromCorner(width: Int, height: Int): Rectangle =
        fromPoint(0, 0, width, height)

object Square:
    def fromPoint(x: Int, y: Int, side: Int): Square =
        new Square(Point(x, y), Point(x + side, y), Point(x + side, y + side), Point(x, y + side))

    def fromCorner(size: Int): Square =
        fromPoint(0, 0, size)

object FigureUtils:
    def areaSum(figures: List[Figure]): Double =
        figures.map(_.area).sum

    def printAll(figures: List[Figure]): Unit =
        figures.foreach(a => println(a.description))
