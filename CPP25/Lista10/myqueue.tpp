namespace adt
{
    // Konstruktor domyślny
    template <typename T>
    myqueue<T>::myqueue() : mylist<T>() {}

    // Destruktor
    template <typename T>
    myqueue<T>::~myqueue() {}

    // Konstruktor z listą inicjalizującą
    template <typename T>
    myqueue<T>::myqueue(std::initializer_list<T> init) : mylist<T>(init) {}

    // Konstruktor kopiujący
    template <typename T>
    myqueue<T>::myqueue(const myqueue<T>& other) : mylist<T>(other) {}

    // Konstruktor przenoszący
    template <typename T>
    myqueue<T>::myqueue(myqueue<T>&& other) : mylist<T>(std::move(other)) {}

    // Przypisanie kopiujące
    template <typename T>
    myqueue<T>& myqueue<T>::operator=(const myqueue<T>& other) {
        if (this != &other)
            mylist<T>::operator=(other);
        return *this;
    }

    // Przypisanie przenoszące
    template <typename T>
    myqueue<T>& myqueue<T>::operator=(myqueue<T>&& other) {
        if (this != &other)
            mylist<T>::operator=(std::move(other));
        return *this;
    }

    // Dodanie elementu na koniec kolejki
    template <typename T>
    void myqueue<T>::enqueue(const T& value) {
        mylist<T>::append(value);
    }

    // Zabranie elementu z początku kolejki
    template <typename T>
    T myqueue<T>::dequeue() {
        if (mylist<T>::isEmpty())
            throw std::runtime_error("Pusta kolejka.");
        T res = mylist<T>::getData(0); 
        mylist<T>::pop(0);
        return res;
    }

    // Wypisywanie zawartości kolejki
    template <typename U>
    std::ostream& operator<<(std::ostream& out, const myqueue<U>& other) {
        out << static_cast<mylist<U>>(other);
        return out;
    }
}
