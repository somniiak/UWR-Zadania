namespace adt
{
    // Konstruktor domyślny
    template <typename T>
    mystack<T>::mystack() : mylist<T>() {}

    // Destruktor
    template <typename T>
    mystack<T>::~mystack() {}

    // Konstruktor z listą inicjalizującą
    template <typename T>
    mystack<T>::mystack(std::initializer_list<T> init) : mylist<T>(init) {}

    // Konstruktor kopiujący
    template <typename T>
    mystack<T>::mystack(const mystack<T>& other) : mylist<T>(other) {}

    // Konstruktor przenoszący
    template <typename T>
    mystack<T>::mystack(mystack<T>&& other) : mylist<T>(std::move(other)) {}

    // Przypisanie kopiujące
    template <typename T>
    mystack<T>& mystack<T>::operator=(const mystack<T>& other) {
        if (this != &other)
            mylist<T>::operator=(other);
        return *this;
    }

    // Przypisanie przenoszące
    template <typename T>
    mystack<T>& mystack<T>::operator=(mystack<T>&& other) {
        if (this != &other)
            mylist<T>::operator=(std::move(other));
        return *this;
    }

    // Dodanie elementu na stos
    template <typename T>
    void mystack<T>::push(const T& value) {
        mylist<T>::prepend(value);
    }

    // Zabranie elementu ze stosu
    template <typename T>
    T mystack<T>::take() {
        if (mylist<T>::isEmpty())
            throw std::runtime_error("Pusty stos.");
        T res = mylist<T>::getData(0); 
        mylist<T>::pop(0);
        return res;
    }

    // Wypisywanie zawartości stosu
    template <typename U>
    std::ostream& operator<<(std::ostream& out, const mystack<U>& other) {
        out << static_cast<mylist<U>>(other);
        return out;
    }
}
