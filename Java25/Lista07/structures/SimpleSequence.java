package structures;

public interface SimpleSequence<T extends Comparable<T>> {
    // Dodanie elementu na zadaną pozycję
    void insert(T el, int pos);

    // Usunięcie pierwszego elementu o zadanej wartości
    void remove(T el);

    // Usunięcie elementu ze wskazanej pozycji
    void remove(int pos);

    // Najmniejszy element
    T min();
    
    // Największy element
    T max();

    // Sprawdzenie czy istnieje element o zadanej wartości
    boolean search(T el);

    // Pobranie elementu z określonej pozycji
    T at(int pos);

    // Wskazanie pozycji elementu o zadanej wartości
    int index(T el);

    // Liczba elementów
    int size();

    // Sprawdzenie czy ciąg jest pusty
    boolean empty();
}
