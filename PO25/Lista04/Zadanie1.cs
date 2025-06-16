// Artur Dzido
// Zadanie 1, Lista 4
// (Zadnia 3, Lista 3)
// (Mono 6.14.0)


using System;
using System.Collections;
using System.Collections.Generic;

// Klasa bazowa dla formuł logicznych.
// abstract - można ją używać tylko jako
// bazową dla innych klas, metody muszą być
// zaimplementowane w klasach pochodnych (override).
abstract class Formula : IEnumerable<Formula> {
    public abstract bool Oblicz(Dictionary<string, bool> zmienne);
    public abstract Formula Simplify();
    public abstract override string ToString();

    public abstract override bool Equals(object obj);
    // GetHashCode() wymaga zmiany przy zmianie Equals
    // https://learn.microsoft.com/en-us/dotnet/api/system.object?view=net-9.0: ^ to XOR dwóch wartości
    public abstract override int GetHashCode();

    // Metody umożliwiające iterację
    public abstract IEnumerator<Formula> GetEnumerator();
    IEnumerator IEnumerable.GetEnumerator() {
        return GetEnumerator();
    }

    // Przeciążenie operatora dla koniunkcji (And)
    public static Formula operator &(Formula left, Formula right) { return new And(left, right); }
    // Przeciążenie operatora dla alternatywy (Or)
    public static Formula operator |(Formula left, Formula right) { return new Or(left, right); }
    // Przeciążenie operatora dla negacji (Not)
    public static Formula operator !(Formula argument) { return new Not(argument); }
}

// Stałe (True, False)
sealed class Stala : Formula {
    private bool value;
    private Stala(bool value) => this.value = value;
    private static readonly Stala trueInstance = new Stala(true);
    private static readonly Stala falseInstance = new Stala(false);
    public static Stala GetInstance(bool value) => value ? trueInstance : falseInstance;
    public override bool Oblicz(Dictionary<string, bool> zmienne) => value;
    public override Formula Simplify() => this;
    public override string ToString() {
        if (value)
            return "True";
        return "False";
    }
    public override bool Equals(object obj) => obj is Stala s && s.value == value;
    public override int GetHashCode() => value.GetHashCode();
    public override IEnumerator<Formula> GetEnumerator() { yield return this; }
}

// Zmienne
sealed class Zmienna : Formula {
    private string name;
    private Zmienna(string name) => this.name = name;
    private static readonly Dictionary<string, Zmienna> instances = new Dictionary<string, Zmienna>();
    public static Zmienna GetInstance(string name) {
        if (!instances.ContainsKey(name))
            instances[name] = new Zmienna(name);
        return instances[name];
    }
    public override bool Oblicz(Dictionary<string, bool> zmienne) => zmienne[name];
    public override Formula Simplify() => this;
    public override string ToString() => name;
    public override bool Equals(object obj) => obj is Zmienna z && z.name == name;
    public override int GetHashCode() => name.GetHashCode();
    public override IEnumerator<Formula> GetEnumerator() { yield return this; }
}

// Negacja
class Not : Formula {
    private Formula argument;
    public Not(Formula argument) => this.argument = argument;
    public override bool Oblicz(Dictionary<string, bool> zmienne) => !argument.Oblicz(zmienne);
    public override Formula Simplify() {
        Formula simplified_argument = argument.Simplify();

        // True -> False
        // False -> True
        if (simplified_argument is Stala s)
            return Stala.GetInstance(!s.Oblicz(new Dictionary<string, bool>()));

        // Podwójna negacja
        if (simplified_argument is Not n)
            return n.argument;

        return new Not(simplified_argument);
    }
    public override string ToString() {
        if (argument is Zmienna z)
            return "¬" + z.ToString();
        return "¬(" + argument.ToString() + ")";
    }
    public override bool Equals(object obj) => obj is Not n && n.argument.Equals(argument);
    public override int GetHashCode() => argument.GetHashCode();
    public override IEnumerator<Formula> GetEnumerator() {
        yield return this;
        foreach (Formula f in argument)
            yield return f;
    }
}

// Koniunkcja
class And : Formula {
    private Formula left, right;
    public And(Formula left, Formula right) {
        this.left = left;
        this.right = right;
    }
    public override bool Oblicz(Dictionary<string, bool> zmienne) => left.Oblicz(zmienne) && right.Oblicz(zmienne);
    public override Formula Simplify() {
        Formula simplified_left = left.Simplify();
        Formula simplified_right = right.Simplify();

        // False ^ simplified_right -> False
        if (simplified_left is Stala scl1 &&
            !scl1.Oblicz(new Dictionary<string,bool>()))
            return Stala.GetInstance(false);

        // True ^ simplified_right -> simplified_right
        if (simplified_left is Stala scl2 &&
            scl2.Oblicz(new Dictionary<string,bool>()))
            return simplified_right;

        // False ^ simplified_left -> False
        if (simplified_right is Stala scr1 &&
            !scr1.Oblicz(new Dictionary<string,bool>()))
            return Stala.GetInstance(false);

        // True ^ simplified_left -> simplified_left
        if (simplified_right is Stala scr2 &&
            scr2.Oblicz(new Dictionary<string,bool>()))
            return simplified_left;

        // simplified_left ^ ¬simplified_left -> False
        if (simplified_left is Zmienna slz1 &&
            simplified_right is Not sr &&
            new Not(sr).Simplify() is Zmienna srz1 &&
            slz1.ToString() == srz1.ToString())
            return Stala.GetInstance(false);

        // ¬simplified_right ^ simplified_right -> False
        if (simplified_right is Zmienna srz2 &&
            simplified_left is Not sl &&
            new Not(sl).Simplify() is Zmienna slz2 &&
            slz2.ToString() == srz2.ToString())
            return Stala.GetInstance(false);

        return new And(simplified_left, simplified_right);
    }
    public override string ToString() => "(" + left.ToString() + " ^ " + right.ToString() + ")";
    public override bool Equals(object obj) => obj is And a && a.left.Equals(left) && a.right.Equals(right);
    public override int GetHashCode() => left.GetHashCode() ^ right.GetHashCode();
    public override IEnumerator<Formula> GetEnumerator() {
        yield return this;
        foreach (Formula f in left)
            yield return f;
        foreach (Formula f in right)
            yield return f;
    }
}

// Alternatywa
class Or : Formula {
    private Formula left, right;
    public Or(Formula left, Formula right) {
        this.left = left;
        this.right = right;
    }
    public override bool Oblicz(Dictionary<string, bool> zmienne) => left.Oblicz(zmienne) || right.Oblicz(zmienne);
    public override Formula Simplify() {
        Formula simplified_left = left.Simplify();
        Formula simplified_right = right.Simplify();

        // True v simplified_right -> True
        if (simplified_left is Stala scl1 &&
            scl1.Oblicz(new Dictionary<string,bool>()))
            return Stala.GetInstance(true);

        // False v simplified_right -> simplified_right
        if (simplified_left is Stala scl2 &&
            !scl2.Oblicz(new Dictionary<string,bool>()))
            return simplified_right;

        // True v simplified_left -> True
        if (simplified_right is Stala scr1 &&
            scr1.Oblicz(new Dictionary<string,bool>()))
            return Stala.GetInstance(true);

        // False v simplified_left -> simplified_left
        if (simplified_right is Stala scr2 &&
            !scr2.Oblicz(new Dictionary<string,bool>()))
            return simplified_left;

        // simplified_left v ¬simplified_left -> True
        if (simplified_left is Zmienna slz1 &&
            simplified_right is Not sr &&
            new Not(sr).Simplify() is Zmienna srz1 &&
            slz1.ToString() == srz1.ToString())
            return Stala.GetInstance(true);

        // ¬simplified_right v simplified_right -> True
        if (simplified_right is Zmienna srz2 &&
            simplified_left is Not sl &&
            new Not(sl).Simplify() is Zmienna slz2 &&
            slz2.ToString() == srz2.ToString())
            return Stala.GetInstance(true);

        return new Or(simplified_left, simplified_right);
    }
    public override string ToString() => "(" + left.ToString() + " v " + right.ToString() + ")";
    public override bool Equals(object obj) => obj is Or o && o.left.Equals(left) && o.right.Equals(right);
    public override int GetHashCode() => left.GetHashCode() ^ right.GetHashCode();
    public override IEnumerator<Formula> GetEnumerator() {
        yield return this;
        foreach (Formula f in left)
            yield return f;
        foreach (Formula f in right)
            yield return f;
    }
}

class Program
{
    static void Main()
    {
        Dictionary<string, bool> zmienne =
        new Dictionary<string, bool> {
            {"x", true},
            {"y", false},
        };

        foreach(var item in zmienne) { Console.Write($" [{item.Key} / {item.Value}]"); }
        Console.WriteLine("\n");

        // ¬x ∨ (y ∧ true)
        Formula zdanie1 = !Zmienna.GetInstance("x") | (Zmienna.GetInstance("y") & Stala.GetInstance(true));
        Console.Write("f1: " + zdanie1.ToString() + ":");
        Console.Write(zdanie1.Oblicz(zmienne) + "\n");
        Formula zdanie1prim = new And(Zmienna.GetInstance("x"), Zmienna.GetInstance("y"));
        Console.Write("f1': " + zdanie1prim.ToString() + ":");
        Console.Write(zdanie1prim.Oblicz(zmienne) + "\n");
        Console.Write("f1 == f1': " + zdanie1.Equals(zdanie1prim) + "\n");

        Formula zdanie2 = !(Zmienna.GetInstance("x") & !(Zmienna.GetInstance("x")));
        Console.Write("f2: " + zdanie2.ToString() + ":");
        Console.Write(zdanie2.Oblicz(zmienne) + "\n");
        Formula zdanie2prim = !(Zmienna.GetInstance("x") & !(Zmienna.GetInstance("x")));
        Console.Write("f2': " + zdanie2prim.ToString() + ":");
        Console.Write(zdanie2prim.Oblicz(zmienne) + "\n");
        Console.Write("f2 == f2': " + zdanie2.Equals(zdanie2prim) + "\n");

        Formula s1 = Stala.GetInstance(true);
        Formula s2 = Stala.GetInstance(false);
        Console.Write($"{s1} i {s2} są tym samym obiektem: {s1 == s2}\n");
        Formula z1 = Zmienna.GetInstance("x");
        Formula z2 = Zmienna.GetInstance("x");
        Console.Write($"{z1} i {z2} są tym samym obiektem: {z1 == z2}\n");

        Formula zdanie3 = !(Zmienna.GetInstance("x") & !(!Zmienna.GetInstance("x") & Zmienna.GetInstance("y")));
        Console.Write("Elementy formuły " + zdanie3.ToString() + ":\n"); int cnt = 1;
        foreach (Formula f in zdanie3) { Console.WriteLine($"{cnt++}. {f}"); }
    }
}