// Artur Dzido
// Zadanie 3, Lista 3
// (Mono 6.14.0)


using System;
using System.Collections.Generic; // Słownik

// Klasa bazowa dla formuł logicznych.
// abstract - można ją używać tylko jako
// bazową dla innych klas, metody muszą być
// zaimplementowane w klasach pochodnych (override).
abstract class Formula {
    public abstract bool Oblicz(Dictionary<string, bool> zmienne);
    public abstract Formula Simplify();
}

// Stałe (True, False)
class Stala : Formula {
    private bool value;
    public Stala(bool value) => this.value = value;
    public override bool Oblicz(Dictionary<string, bool> zmienne) => value;
    public override Formula Simplify() => this;
}

// Zmienne
class Zmienna : Formula {
    private string name;
    public Zmienna(string name) => this.name = name;
    public override bool Oblicz(Dictionary<string, bool> zmienne) => zmienne[name];
    public override Formula Simplify() => this;
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
            return new Stala(!s.Oblicz(new Dictionary<string, bool>()));

        // Podwójna negacja
        if (simplified_argument is Not n)
            return n.argument;

        return new Not(simplified_argument);
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
            return new Stala(false);

        // True ^ simplified_right -> simplified_right
        if (simplified_left is Stala scl2 &&
            scl2.Oblicz(new Dictionary<string,bool>()))
            return simplified_right;

        // False ^ simplified_left -> False
        if (simplified_right is Stala scr1 &&
            !scr1.Oblicz(new Dictionary<string,bool>()))
            return new Stala(false);

        // True ^ simplified_left -> simplified_left
        if (simplified_right is Stala scr2 &&
            scr2.Oblicz(new Dictionary<string,bool>()))
            return simplified_left;

        return new And(simplified_left, simplified_right);
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
            return new Stala(true);

        // False v simplified_right -> simplified_right
        if (simplified_left is Stala scl2 &&
            !scl2.Oblicz(new Dictionary<string,bool>()))
            return simplified_right;

        // True v simplified_left -> True
        if (simplified_right is Stala scr1 &&
            scr1.Oblicz(new Dictionary<string,bool>()))
            return new Stala(true);

        // False v simplified_left -> simplified_left
        if (simplified_right is Stala scr2 &&
            !scr2.Oblicz(new Dictionary<string,bool>()))
            return simplified_left;

        return new Or(simplified_left, simplified_right);
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

        foreach(var item in zmienne) {
            Console.Write($" [{item.Key} / {item.Value}]");
            }
        Console.WriteLine("\n");

        // ¬x ∨ (y ∧ true)
        Formula zdanie1 = new Or(new Not(new Zmienna("x")), new And(new Zmienna("y"), new Stala(true)));
        Console.Write("¬x ∨ (y ∧ true): ");
        Console.Write(zdanie1.Oblicz(zmienne));
        Console.WriteLine();

        // x v false
        Formula zdanie2 = new Or(new Zmienna("x"), new Stala(false));
        Console.Write("x v false: ");
        Console.Write(zdanie2.Oblicz(zmienne));
        Console.WriteLine();
    }
}