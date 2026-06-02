package numbers

class Rational private (_n: Int, _d: Int):
    require(_d != 0, "Denominator cannot be zero")

    private val g = gcd(_n, _d)
    val n = (if _d < 0 then -_n else _n) / g
    val d = Math.abs(_d) / g

    private def gcd(a: Int, b: Int): Int =
        if (b == 0) a.abs else gcd(b, a % b)

    def +(other: Rational): Rational =
        Rational(n * other.d + other.n * d, d * other.d)

    def -(other: Rational): Rational =
        Rational(n * other.d - other.n * d, d * other.d)

    def *(other: Rational): Rational =
        Rational(n * other.n, d * other.d)

    def /(other: Rational): Rational =
        require(other.n != 0, "Division by zero")
        Rational(n * other.d, other.n * d)

    def toDouble: Double =
        n.toDouble / d

    def toTuple: (Int, Int) =
        (n, d)

    override def toString: String =
        val num = n / d
        val rem = (n % d).abs

        if (rem == 0) s"$num"
        else if (num == 0) s"$rem/$d"
        else s"$num $rem/$d"

    override def equals(other: Any): Boolean =
        if other.isInstanceOf[Rational] then
            val r = other.asInstanceOf[Rational]
            n == r.n && d == r.d
        else false


object Rational:
    def apply(n: Int, d: Int = 1): Rational =
        new Rational(n, d)

    val zero: Rational =
        new Rational(0, 1)

    val one: Rational =
        new Rational(1, 1)
