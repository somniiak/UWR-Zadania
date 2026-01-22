import figury.*;

public class TestFigur {
    public static void main(String[] args) {
        // Punkt
        Punkt p1 = new Punkt(0, 0);
        Punkt p2 = new Punkt(3, 0);
        Punkt p3 = new Punkt(5, 1);

        // Wektor
        Wektor w1 = new Wektor(2, 3);
        Wektor w2 = new Wektor(1, 1);
        Wektor zlozony = Wektor.addVectors(w1, w2);
        System.out.println("Złożenie wektorów " + w1 + " i " + w2 + ": " + zlozony);
        System.out.println();
        
        // Prosta
        Prosta pr1 = new Prosta(1, 0, 0);
        Prosta pr2 = new Prosta(0, 1, 0);
        System.out.println("Prosta 1: " + pr1);
        System.out.println("Prosta 2: " + pr2);
        System.out.println("Czy proste prostopadłe? " + Prosta.arePerpendicular(pr1, pr2));
        System.out.println("Czy proste równoległe? " + Prosta.areParallel(pr1, pr2));
        Punkt przeciecie = Prosta.getIntersection(pr1, pr2);
        System.out.println("Punkt przecięcia: " + przeciecie);
        System.out.println();

        // Odcinek
        Odcinek odc = new Odcinek(p1, p2);
        System.out.println("Odcinek przed przesunięciem: " + odc);
        odc.przesun(w1);
        System.out.println("Odcinek po przesunięciu: " + odc);
        odc.obroc(p2, 60);
        System.out.println("Odcinek po obrocie: " + odc);
        odc.odbij(pr1);
        System.out.println("Odcinek po odbiciu: " + odc);
        System.out.println();

        // Trójkąt
        Trojkat tr = new Trojkat(p1, p2, p3);
        System.out.println("Trójkąt przed przesunięciem: " + tr);
        tr.przesun(w1);
        System.out.println("Trójkąt po przesunięciu: " + tr);
        tr.obroc(p2, 60);
        System.out.println("Trójkąt po obrocie: " + tr);
        tr.odbij(pr1);
        System.out.println("Trójkąt po odbiciu: " + tr);
        System.out.println();
    }
}