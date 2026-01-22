import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.function.BinaryOperator;
import java.util.function.UnaryOperator;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    // https://pysaumont.github.io/2014/09/01/Recursive-lambdas-in-Java-8.html

    static  final UnaryOperator<Integer> collatz = n ->
            n == 1 ? 1 : 1 + Main.collatz.apply(n % 2 == 0 ? n / 2: 3 * n + 1);

    final BinaryOperator<Integer> gcd =(a, b) ->
            b == 0 ? a : this.gcd.apply(b, a % b);

    public static void partOne() {
        ArrayList<Integer> numbers = new ArrayList<>();

        String validate = "^(?<number>\\d*)(//(?<comment>.*))?$";
        Pattern validator = Pattern.compile(validate);

        try (BufferedReader br = new BufferedReader(
                new FileReader("sample_1.txt"))) {
            for (String line = br.readLine(); line != null; line = br.readLine()) {
                line = line.trim();

                Matcher matcher = validator.matcher(line);

                if (!matcher.matches())
                    throw new IllegalArgumentException("Regex nie pasuje: " + line);

                String numberMatch = matcher.group("number");

                if (numberMatch.isEmpty()) continue;
                // https://stackoverflow.com/a/2800839
                // Znajdowanie wiodących zer
                if (numberMatch.matches("^0+(?!$)"))
                    throw new IllegalArgumentException("Liczba zawiera wiodące zera.");

                try {
                    int number = Integer.parseInt(numberMatch);

                    if (number < 1 || number > 1_000_000_000)
                        throw new IllegalArgumentException("Liczba poza zakresem: " + number);

                    numbers.add(number);
                } catch (NumberFormatException e) {
                    throw new IllegalArgumentException("Nieprawidłowa liczba: " + numberMatch);
                }
            }

            if (numbers.size() < 20)
                throw new IllegalStateException("Plik nie zawiera przynajmniej 20 liczb.");

        } catch (Exception ex) {
            System.err.println(ex.getMessage());
        }

        System.out.println("\n===== CZĘŚĆ 1 ======");

        System.out.println("\nOd największej do najmniejszej:");
        numbers.stream()
                .sorted((a, b) -> b - a)
                .forEach(System.out::println);

        System.out.println("\nLiczby pierwsze:");
        numbers.stream()
                .filter(n -> {
                    if (n <= 1) return false;

                    for (int i = 2; i <= Math.sqrt(n); i++)
                        if (n % i == 0)
                            return false;

                    return true;
                }).forEach(System.out::println);;

        System.out.println("\nSuma liczb mniejszych od n = 80000000: " +
                numbers.stream()
                        .filter(n -> n < 80000000)
                        .mapToInt(Integer::intValue)
                        .sum()
        );

        System.out.println("\nPodzielnych przez n = 7: " +
            numbers.stream()
                .filter(n -> n % 7 == 0)
                .count()
        );
    }

    public static void partTwo() {
        LinkedList<Trojkat> triangles = new LinkedList<>();

        String validate = "^\\s*(\\d+\\.?\\d*(\\s+)?){0,}(//.*)?$";
        Pattern validator = Pattern.compile(validate);

        String extract = "^(?<num1>\\d+\\.?\\d*) (?<num2>\\d+\\.?\\d*) (?<num3>\\d+\\.?\\d*)(//.*)?$";
        Pattern extractor = Pattern.compile(extract);

        try (BufferedReader br = new BufferedReader(
                new FileReader("sample_2.txt"))) {
            for (String line = br.readLine(); line != null; line = br.readLine()) {
                line = line.trim();

                if (!validator.matcher(line).matches())
                    throw new IllegalArgumentException("Regex nie pasuje: " + line);

                Matcher matcher = extractor.matcher(line);
                // Nie zawiera dokładnie trójki liczb
                if (!matcher.matches())
                    continue;

                double x = Double.parseDouble(matcher.group("num1"));
                double y = Double.parseDouble(matcher.group("num2"));
                double z = Double.parseDouble(matcher.group("num3"));

                Trojkat triangle;

                try {
                    triangle = new Trojkat(x, y, z);
                } catch (Exception e) {
                    continue;
                }

                triangles.add(new Trojkat(x, y, z));
            }
        } catch (Exception ex) {
            System.err.println(ex.getMessage());
        }

        System.out.println("\n===== CZĘŚĆ 2 ======");

        System.out.println("\nOd najmniejszego do największego obwodu:");
        triangles.stream()
                .sorted((t1, t2) ->
                        Double.compare(t1.x + t1.y + t1.z, t2.x + t2.y + t2.z))
                .forEach(System.out::println);

        System.out.println("\nTrójkąty prostokątne:");
        triangles.stream()
                .filter(t -> {
                   double max = Math.max(t.x, Math.max(t.y, t.z));
                   double eps = 0.000001;

                    if (max == t.x)
                       return Math.abs(t.y * t.y + t.z * t.z - max * max) < eps;
                   else if (max == t.y)
                        return Math.abs(t.x * t.x + t.z * t.z - max * max) < eps;
                   else
                       return  Math.abs(t.x * t.x + t.y * t.y - max * max) < eps;
                }).forEach(System.out::println);

        System.out.println("\nTrójkąty równoboczne: " +
                triangles.stream()
                        .filter(t -> t.x == t.y && t.y == t.z && t.x == t.z)
                        .count()
        );

        System.out.println("\nNajmniejsze pole:");
        triangles.stream()
                .min((t1, t2) -> {
                    double p1 = 0.5 * (t1.x + t1.y + t1.z);
                    double p2 = 0.5 * (t2.x + t2.y + t2.z);

                    double s1 = Math.sqrt(
                            p1 * (p1 - t1.x) * (p1 - t1.y) * (p1 - t1.z));

                    double s2 = Math.sqrt(
                            p2 * (p2 - t2.x) * (p2 - t2.y) * (p2 - t2.z));

                    return Double.compare(s1, s2);
                }).ifPresent(System.out::println);

        System.out.println("\nNajwiększe pole:");
        triangles.stream()
                .max((t1, t2) -> {
                    double p1 = 0.5 * (t1.x + t1.y + t1.z);
                    double p2 = 0.5 * (t2.x + t2.y + t2.z);

                    double s1 = Math.sqrt(
                            p1 * (p1 - t1.x) * (p1 - t1.y) * (p1 - t1.z));

                    double s2 = Math.sqrt(
                            p2 * (p2 - t2.x) * (p2 - t2.y) * (p2 - t2.z));

                    return Double.compare(s1, s2);
                }).ifPresent(System.out::println);
    }

    public static void main(String[] args) {
        Main m = new Main();

        partOne();
        partTwo();

        System.out.println("\n===== CZĘŚĆ 3 ======");
        System.out.println("Collatz n = 11: " + collatz.apply(11));
        System.out.println("NWD(15, 25): " + m.gcd.apply(15, 25));
    }
}