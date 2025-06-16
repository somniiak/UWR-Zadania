// Artur Dzido
// Zadanie 1, Lista 2
// (Mono 6.14.0)


using System;

public class IntStream
{
    public int value;
    public bool isEndOfStream;

    // Konstruktor
    public IntStream()
    {
        value = 0;
        isEndOfStream = false;
    }

    // Kolejna liczba naturalna
    public virtual int next()
    {
        if (isEndOfStream)
        {
            Console.WriteLine("Strumień zakończony.");
        }

        else
            value++;

        return value;
    }

    // Koniec strumienia
    public bool eos()
    {
        return isEndOfStream;
    }

    // Resetowanie strumienia
    public virtual void reset()
    {
        value = 0;
        isEndOfStream = false;
    }
}

public class FibStream : IntStream
{
    int prev1;
    int prev2;

    public FibStream()
    {
        prev1 = 0;
        prev2 = 1;
        value = 0;
        isEndOfStream = false;
    }

    public override int next()
    {
        int next = prev1 + prev2;

        if (next < prev1 || next < prev2) // Przepełnienie
            isEndOfStream = true;

        if (isEndOfStream)
            Console.WriteLine("Strumień zakończony.");

        else
        {
        prev1 = prev2;
        prev2 = next;
        value = next;
        }

        return value;
    }

    public override void reset()
    {
        prev1 = 0;
        prev2 = 1;
        value = 0;
        isEndOfStream = false;
    }

}

public class RandomStream : IntStream
{
    public RandomStream()
    {
        value = 0;
        isEndOfStream = false;
    }

    public override int next()
    {
        if (isEndOfStream)
        {
            Console.WriteLine("Strumień zakończony.");
        }

        else
        {
            Random random = new Random();
            value = random.Next();
        }

        return value;
    }

}

public class RandomWordStream
{
    public FibStream length;
    private RandomStream random;
    public string value;
    private string alphabet = "abcdefghijklmnopqrstuvwxyz";
    bool isEndOfStream;

    public RandomWordStream()
    {
        value = "";
        length = new FibStream();
        random = new RandomStream();
        isEndOfStream = false;
    }

    public string next()
    {
        value = ""; length.next();

        for (int i = 0; i < length.value; i++)
        {
            value += alphabet[random.next() % 26];
        }

        return value;
    }

    public bool eos()
    {
        return isEndOfStream;
    }

    public virtual void reset()
    {
        value = "";
        isEndOfStream = false;
    }
}

class Program
{
    static void Main()
    {
        // Przykład użycia IntStream
        IntStream stream = new IntStream(); Console.WriteLine(stream.value); // 0
        stream.next(); Console.WriteLine(stream.value); // 1
        stream.next(); Console.WriteLine(stream.value); // 2
        stream.next(); Console.WriteLine(stream.value); // 3

        // Resetowanie strumienia
        stream.reset();
        Console.WriteLine(stream.value);
        Console.WriteLine(stream.isEndOfStream);
        stream.next();
        Console.WriteLine(stream.value);


        // Przykład użycia FibStream
        FibStream fs = new FibStream();
        while(!fs.eos())
        {
            Console.Write(fs.next() + " ");
        }
        Console.WriteLine();
        fs.reset(); fs.next();
        Console.WriteLine(fs.value);


        // Przykład użycia RandomStream
        RandomStream rs = new RandomStream();
        for (int i = 0; i < 100; i++)
        {
            Console.Write(rs.next() + " ");
        }
        Console.WriteLine();


        // Przykład użycia RandomWordStream
        RandomWordStream ws = new RandomWordStream();
        for (int i = 0; i < 10; i++)
        {
            Console.WriteLine(ws.next());
        }
    }
}