object Utils:
    // Nil - empty list; _ :: Nil - list has one element 
    def isSorted(as: List[Int], ordering: (Int, Int) => Boolean): Boolean =
        as match
            case Nil | _ :: Nil => true
            case hd :: second :: tl => ordering(hd, second) && isSorted(tl, ordering)

    def isAscSorted(as: List[Int]): Boolean =
        isSorted(as, _ <= _)

    def isDescSorted(as: List[Int]): Boolean =
        isSorted(as, (a: Int, b: Int) => a >= b)

    def foldLeft[A, B](l: List[A], z: B)(f: (B, A) => B): B =
        def aux(as: List[A], acc: B): B = as match
            case Nil => acc
            case hd :: tl => aux(tl, f(acc, hd))
        aux(l, z)

    def sum(l: List[Int]): Int =
        foldLeft(l, 0)(_ + _)

    def length[A](l: List[A]): Int =
        foldLeft(l, 0)(_ + 1)

    def compose[A, B, C](f: B => C, g: A => B): (A => C) =
        (x: A) => f(g(x))

    // If we want to apply 'f', a few times
    // its signature should be f: A => A?
    def repeated[A](f: A => A, n: Int): A => A =
        foldlef(List.fill(n)(f), identity[A] {compose(...)}
        (x: A) => (0 until n).foldLeft(x)((acc, _) => f(acc))

    def curry[A, B, C](f: (A, B) => C): A => B => C =
        (a: A) => (b: B) => f(a, b)

    def uncurry[A, B, C](f: A => B => C): (A, B) => C =
        (a: A, b: B) => f(a)(b)

def unSafe[T](ex: Exception)(body: => T): T =
    try { body } catch {
        case e: Exception => {
            println(s"Exception occured: ${e.getMessage}")
            throw ex
        }
    }

object Solution extends App:
    val xs = List(42, 67, 69, 420, 2137)
    println(s"$xs - ascending?: ${ Utils.isAscSorted(xs) }")
    println(s"$xs - descending?: ${ Utils.isDescSorted(xs) }")
    println(s"$xs - sum: ${ Utils.sum(xs) }")
    println(s"$xs - length: ${ Utils.length(xs) }")
    println(s"$xs - fold_left(l, 1L)(_ * _) - product: ${ Utils.foldLeft(xs, 1L)(_ * _) }")
    println(s"compose: x * x -> x * 1 (x = 2): ${ Utils.compose((x: Int) => x + 1, (x: Int) => x * x)(2)}")
    println(s"f(x) = x * 5; 4 times: ${ Utils.repeated((x: Int) => x * 5, 4)(1) }")
    val add = (a: Int, b: Int) => a + b
    val addCurried = Utils.curry(add)
    val addUncurried = Utils.uncurry(addCurried)
    println(s"addCurreid(1)(1): ${ addCurried(1)(1) }")
    println(s"addUncurried(1, 1): ${ addUncurried(1, 1) }")
    unSafe(new Exception("Testing exception")):
        0 / 0