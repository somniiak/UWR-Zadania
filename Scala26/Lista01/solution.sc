import scala.math.sqrt
import scala.io.Source.fromFile
import scala.util.matching.Regex

// Scalar product of two vectors xs and ys
def scalarUgly(xs: List[Int], ys: List[Int]) = {
    require(xs.size == ys.size)

    var res = 0
    var idx = 0

    while (idx < xs.size) {
        res += xs(idx) * ys(idx)
        idx += 1
    }

    res
}

println("\nscalarUgly([1, 2, 3, 4], [5, 6, 7, 8]):")
println(scalarUgly(List(1, 2, 3, 4), List(5, 6, 7, 8)))

def scalar(xs: List[Int], ys: List[Int]) = {
    require(xs.size == ys.size)

    val nums = for {
        (x, y) <- xs zip ys
    } yield x * y

    nums.foldLeft(0)(_ + _)
}

println("\nscalar([1, 2, 3, 4], [5, 6, 7, 8]):")
println(scalar(List(1, 2, 3, 4), List(5, 6, 7, 8)))

// Quicksort algorithm (w obu pivot to hd)
def sortUgly(xs: List[Int]): List[Int] =
    xs match {
        case Nil => Nil
        case hd :: tl => {
            var i = 1
            var leq = List.empty[Int]
            var gt = List.empty[Int]

            while (i < xs.size) {
                if (xs(i) <= hd) then
                    leq = xs(i) +: leq
                else
                    gt = gt :+ xs(i)
                i += 1
            }

            sortUgly(leq) ::: (hd +: sortUgly(gt))
        }
    }

println("\nsortUgly([1, 7, 3, 0, 5, 9, 3]):")
println(sortUgly(List(1, 7, 3, 0, 5, 9, 3)))

def sort(xs: List[Int]): List[Int] = {
    xs match {
        case Nil => Nil
        case hd :: tl =>
            val leq = for {
                x <- tl
                if x <= hd
            } yield x

            val gt = for {
                x <- tl
                if x > hd
            } yield x

            sort(leq) ::: (hd +: sort(gt))
    }
}

println("\nsort([1, 7, 3, 0, 5, 9, 3]):")
println(sort(List(1, 7, 3, 0, 5, 9, 3)))

// Checks if n is prime
def isPrimeUgly(n: Int): Boolean = {
    if (n < 2)
        return false

    if (n == 2)
        return true

    var i = 3
    while (i <= math.sqrt(n).toInt) {
        if (n % i == 0)
            return false
        i += 2
    }

    return true
}

println("\nisPrimeUgly(97):")
println(isPrimeUgly(97))

def isPrime(n: Int): Boolean = {
    val bools = for {
        i <- 2 to sqrt(n).toInt
    } yield (n % i == 0)

    !bools.exists(_ == true)
}

println("\nisPrime(97):")
println(isPrime(97))

// For given positive integer n, find all pairs of integers i and j,
// where 1 ≤ j < i < n such that i + j is prime
def primePairsUgly(n : Int): List[(Int, Int)] = {
    var res = List.empty[(Int, Int)]

    var i = 2
    var j = 1

    while (i < n) {
        while (j < i) {
            if isPrime(i + j) then
                res = (i, j) :: res
            j += 1
        }
        i += 1
        j = 1
    }

    res.reverse
}

println("\nprimePairsUgly(7):")
println(primePairsUgly(7))

def primePairs(n : Int): List[(Int, Int)] = {
    val pairs = for {
        i <- 2 until n
        j <- 1 until i
        if isPrime(i + j)
    } yield (i, j)

    pairs.toList
}

println("\nprimePairs(7):")
println(primePairs(7))

// Create a list with all lines from given file
def fileLinesUgly(file: java.io.File): List[String] = {
    var linesIt = fromFile(file).getLines
    var res = List.empty[String]

    while (linesIt.hasNext)
        res = res :+ linesIt.next

    return res
}

// println("\nfileLinesUgly solution.sc:")
// println(fileLinesUgly(new java.io.File("solution.sc")))

def fileLines(file: java.io.File): List[String] =
    fromFile(file).getLines.toList

// println("\nfileLines solution.sc:")
// println(fileLines(new java.io.File("solution.sc")))

// Print names of all .scala files which are in filesHere & are non empty
val filesHere = new java.io.File(".").listFiles

def printNonEmptyUgly(pattern: String): Unit = {
    var filePattern: Regex = pattern.r
    var filesIt = filesHere.iterator
    var file: java.io.File = null

    while(filesIt.hasNext) {
        file = filesIt.next()

        if (file.isFile && file.length != 0) then
            if (filePattern.matches(file.getName)) then
                println(file.getName)
    }
}

println("\nprintNonEmptyUgly:")
printNonEmptyUgly("""^.+\.(?:sc|scala)$""")

def printNonEmpty(pattern: String): Unit = {
    val filePattern: Regex = pattern.r

    val files = for {
        file <- filesHere
        if (file.isFile && file.length != 0)
        if (filePattern.matches(file.getName))
    } println(file.getName)
}

println("\nprintNonEmpty:")
printNonEmpty("""^.+\.(?:sc|scala)$""")
