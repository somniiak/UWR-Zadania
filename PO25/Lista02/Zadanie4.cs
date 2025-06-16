// Artur Dzido
// Zadanie 4, Lista 2
// (Mono 6.14.0)


using System;

public class KolejneSlowaFibonacciego
{
    private string word1;
    private string word2;
    private string prev1;
    private string prev2;

    public KolejneSlowaFibonacciego()
    {
        word1 = "a";
        word2 = "b";
        prev1 = word2;
        prev2 = word1;
    }

    public KolejneSlowaFibonacciego(string slowo1, string slowo2)
    {
        word1 = slowo1;
        word2 = slowo2;
        prev1 = slowo2;
        prev2 = slowo1;
    }

    public string next()
    {
        string noweSlowo = prev1 + prev2;
        prev2 = prev1;
        prev1 = noweSlowo;
        return noweSlowo;
    }
}

public class JakiesSlowaFibonacciego
{
    private string word1;
    private string word2;
    private string[] slowaFibonacciego;
    private int maxIndex;

    public JakiesSlowaFibonacciego()
    {
        word1 = "a";
        word2 = "b";
        slowaFibonacciego = new string[100]; // Maksymalna ilość słow to 100
        slowaFibonacciego[0] = word1;
        slowaFibonacciego[1] = word2;
        maxIndex = 1; // Przechowujemy ilość zapisanych słów
    }

    public JakiesSlowaFibonacciego(string slowo1, string slowo2)
    {
        word1 = slowo1;
        word2 = slowo2;
        slowaFibonacciego = new string[100];
        slowaFibonacciego[0] = word1;
        slowaFibonacciego[1] = word2;
        maxIndex = 1;
    }

    public string slowo(int i)
    {
        while (maxIndex < i)
        {
            slowaFibonacciego[maxIndex + 1] = slowaFibonacciego[maxIndex] + slowaFibonacciego[maxIndex - 1];
            maxIndex++;
        }

        return slowaFibonacciego[i];
    }
}

class Program
{
    static void Main()
    {
        // Użycie konstruktora bezparametrowego
        KolejneSlowaFibonacciego kfib1 = new KolejneSlowaFibonacciego();
        Console.WriteLine(kfib1.next());
        Console.WriteLine(kfib1.next());
        Console.WriteLine(kfib1.next());

        // Użycie konstruktora z parametrami
        KolejneSlowaFibonacciego kfib2 = new KolejneSlowaFibonacciego("x", "y");
        Console.WriteLine(kfib2.next());
        Console.WriteLine(kfib2.next());
        Console.WriteLine(kfib2.next());

        // Użycie konstruktora bezparametrowego
        JakiesSlowaFibonacciego jfib1 = new JakiesSlowaFibonacciego();
        Console.WriteLine(jfib1.slowo(0));
        Console.WriteLine(jfib1.slowo(1));
        Console.WriteLine(jfib1.slowo(2));
        Console.WriteLine(jfib1.slowo(3));
        
        // Użycie konstruktora z parametrami
        JakiesSlowaFibonacciego jfib2 = new JakiesSlowaFibonacciego("x", "y");
        Console.WriteLine(jfib2.slowo(0));
        Console.WriteLine(jfib2.slowo(10));
        Console.WriteLine(jfib2.slowo(5));
    }
}