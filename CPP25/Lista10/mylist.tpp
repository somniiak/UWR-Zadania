namespace adt
{
    // Konstruktor domyślny
    template <typename T>
    mylist<T>::mylist() :
    head(nullptr), tail(nullptr), size(0) {}

    // Destruktor
    template <typename T>
    mylist<T>::~mylist() {
        clear();
    }

    // Konstruktor z listą inicjalizującą
    template <typename T>
    mylist<T>::mylist(std::initializer_list<T> init) :
    head(nullptr), tail(nullptr), size(0) {
        for (const T& item : init) {
            append(item);
        }
    }

    // Konstruktor kopiujący
    template <typename T>
    mylist<T>::mylist(const mylist<T> &other) :
    head(nullptr), tail(nullptr), size(0) {
        mynode* temp = other.head;
        while (temp) {
            append(temp->data);
            temp = temp->next;
        }
    }

    // Konstruktor przenoszący
    template <typename T>
    mylist<T>::mylist(mylist<T>&& other) :
    head(other.head), tail(other.tail), size(other.size) {
        other.head = other.tail = nullptr;
        other.size = 0;
    }

    // Przypisanie kopiujące
    template <typename T>
    mylist<T>& mylist<T>::operator=(const mylist<T>& other) {
        if (this == &other)
            return *this;

        clear();
        mynode* temp = other.head;
        while (temp) {
            append(temp->data);
            temp = temp->next;
        }
        return *this;
    }

    // Przypisanie przenoszące
    template <typename T>
    mylist<T>& mylist<T>::operator=(mylist<T>&& other) {
        if (this != &other) {
            clear();
            head = other.head;
            tail = other.tail;
            size = other.size;
            other.head = nullptr;
            other.tail = nullptr;
            other.size = 0;
        }
        return *this;
    }

    // Czyszczenie zawartości listy
    template <typename T>
    void mylist<T>::clear() {
        while (head) {
            mynode* temp = head;
            head = head->next;
            delete temp;
        }
        head = tail = nullptr;
        size = 0;
    }

    // Wstawienie elementu na początek listy
    template <typename T>
    void mylist<T>::prepend(const T& value) {
        head = new mynode(value, this->head);
        if (tail == nullptr)
            tail = head;
        size++;
    }

    // Wstawienie elementu na koniec listy
    template <typename T>
    void mylist<T>::append(const T& value) {
        mynode* newNode = new mynode(value, nullptr);
        if (head == nullptr)
            head = tail = newNode;
        else {
            tail->next = newNode;
            tail = newNode;
        }
        size++;
    }

    // Wstawienie elementu na zadaną pozycję
    template <typename T>
    void mylist<T>::insert(int idx, const T& value) {
        if (idx < 0 || idx > size)
            throw std::out_of_range("Indeks poza zakresem.");

        if (idx == 0) {
            prepend(value);
            return;
        }

        if (idx == size) {
            append(value);
            return;
        }

        mynode* temp = head;
        for (int cur = 0; cur < idx - 1; cur++)
            temp = temp->next;

        temp->next = new mynode(value, temp->next);
        size++;
    }

    // Usunięcie elementu z końca listy
    template <typename T>
    void mylist<T>::pop() {
        if (size == 0)
            throw std::out_of_range("Lista pusta.");
        pop(size - 1);
    }

    // Usunięcie elementu o określonej pozycji
    template <typename T>
    void mylist<T>::pop(int idx) {
        // Poza zakresem
        if (idx < 0 || idx >= size)
            throw std::out_of_range("Indeks poza zakresem.");

        mynode* toDelete;

        // Usuwanie z przodu
        if (idx == 0) {
            toDelete = head;
            head = head->next;
            if (head == nullptr)
                tail = nullptr;
        }

        // Usuwanie ze środka (lub końca)
        else {
            mynode* temp = head;
            for (int i = 0; i < idx - 1; i++)
                temp = temp->next;

            toDelete = temp->next;
            temp->next = toDelete->next;

            if (toDelete == tail)
                tail = temp;
        }

        delete toDelete;
        size--;
    }

    // Usunięcie elementu o zadanej wartości
    template <typename T>
    void mylist<T>::remove(const T& value) {
        // Jeśli lista pusta
        if (head == nullptr)
            return;

        // Usuwanie z początku
        if (head->data == value) {
            mynode* toDelete = head;
            head = head->next;
            // Lista była jednoelementowa
            if (head == nullptr)
                tail = nullptr;
            delete toDelete;
            size--;
            return;
        }

        mynode* prev = head;
        mynode* curr = head->next;

        // Przeszukiwanie węzłów
        while (curr != nullptr && curr->data != value) {
            prev = curr;
            curr = curr->next;
        }

        // Znaleziono wartość
        if (curr != nullptr) {
            prev->next = curr->next;
            if (curr == tail)
                tail = prev;
            delete curr;
            size--;
        }
    }

    // Usunięcie wszystkich elementów o zadanej wartości
    template <typename T>
    void mylist<T>::filter(const T& value) {
        // Usuwanie z początku
        while (head != nullptr && head->data == value) {
            mynode* toDelete = head;
            head = head->next;
            delete toDelete;
            size--;
        }

        // Lista stała się pusta
        if (head == nullptr) {
            tail = nullptr;
            return;
        }

        mynode* prev = head;
        mynode* curr = head->next;

        // Przeszukiwanie węzłów
        while (curr != nullptr) {
            if (curr->data == value) {
                mynode* toDelete = curr;
                curr = curr->next;
                prev->next = curr;
                delete toDelete;
                size--;
            }
            else {
                prev = curr;
                curr = curr->next;
            }
        }

        // Aktualizacja ogona
        tail = prev;
    }

    // Określenie pozycji elementu o zadanej wartości
    template <typename T>
    int mylist<T>::index(const T& value) const {
        mynode* temp = head;
        int index = 0;

        while (temp != nullptr) {
            if (temp->data == value)
                return index;
            temp = temp->next;
            index++;
        }

        return -1;
    }

    // Policzenie wszystkich elementów o zadanej wartości
    template <typename T>
    int mylist<T>::count(const T& value) const {
        mynode* temp = head;
        int count = 0;

        while (temp != nullptr) {
            if (temp->data == value)
                count++;
            temp = temp->next;
        }

        return count;
    }

    // Zliczenie wszystkich elementów na liście
    template <typename T>
    int mylist<T>::getSize() const {
        return size;
    }

    // Sprawdzenie czy lista jest pusta
    template <typename T>
    bool mylist<T>::isEmpty() const {
        return size == 0;
    }

    // Pobranie wartości
    template <typename T>
    T mylist<T>::getData(int idx) const {
        mynode* temp = head;
        
        for (int i = 0; i < idx; i++)
            temp = temp->next;

        return temp->data;
    }

    // Wypisywanie zawartości listy
    // https://en.cppreference.com/w/cpp/language/friend
    template <typename T>
    std::ostream& operator<<(std::ostream &out, const mylist<T> &other) {
        typename mylist<T>::mynode* temp = other.head;
        out << "[";
        while(temp) {
            out << temp->data;
            if(temp->next)
                out << ", ";
            temp = temp->next;
        }
        out << "]";
        return out;
    }
}
