package Lista01;

import java.util.Scanner;

public class RokUrodzenia
{
    private static String[] rzymskie = {
            "M", "CM", "D", "CD", "C","XC", "L", "XL", "X", "IX", "V", "IV", "I"
        };

    private static int[] arabskie = {
            1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
        };

    private static String[] zwierzeta = {
        "szczur", "bawół", "tygrys", "królik", "smok", "wąż",
        "koń", "owca", "małpa", "kurczak", "pies", "świnia"
    };

    public static String rzymska(int n) {
        if (n <= 0 || n >= 4000)
            throw new IllegalArgumentException("Rok " + n + " spoza zakresu");

        StringBuilder roman = new StringBuilder();

        for (int i = 0; i < arabskie.length; i++) {
            while (n >= arabskie[i]) {
                roman.append(rzymskie[i]);
                n -= arabskie[i];
            }
        }

        return roman.toString();
    }

    public static String patronChinski(int n) {
        int idx = (n - 4) % 12;
        if (idx < 0) idx += 12;
        // return zwierzeta[idx];

        String res = switch(idx) {
            case 0 -> zwierzeta[0];
            case 1 -> zwierzeta[1];
            case 2 -> zwierzeta[2];
            case 3 -> zwierzeta[3];
            case 4 -> zwierzeta[4];
            case 5 -> zwierzeta[5];
            case 6 -> zwierzeta[6];
            case 7 -> zwierzeta[7];
            case 8 -> zwierzeta[8];
            case 9 -> zwierzeta[9];
            case 10 -> zwierzeta[10];
            default -> zwierzeta[11];
        };

        return res;
    }

    public static void main(String[] args)
    {
        String name;
        int year;

        // https://stackoverflow.com/questions/12519335/resource-leak-in-is-never-closed
        try (Scanner input = new Scanner(System.in))
        {
            System.err.print("Imię: ");
            name = input.nextLine();

            System.err.print("Rok urodzenia: ");
            year = input.nextInt();
        }

        System.out.println("Cześć " + name + "!");
        System.out.println("Rok " + year + " w cyfrach rzymskich: " + rzymska(year));
        System.out.println("Patron chiński na rok " + year + ": " + patronChinski(year));
    }
}