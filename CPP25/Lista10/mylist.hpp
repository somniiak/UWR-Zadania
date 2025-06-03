#ifndef MYLIST_HPP
#define MYLIST_HPP

#include <cstring>
#include <iostream>
#include <stdexcept>
#include <initializer_list>

namespace adt
{
    template <typename T>
    class mylist
    {
        private:
            class mynode {
                public:
                    T data;
                    mynode* next;

                    mynode(const T& value) : data(value), next(nullptr) {} // Konstruktor
                    mynode(const T& value, mynode* next_ptr) : data(value), next(next_ptr) {} // Konstruktor kopiujący
                    mynode(T&& value) : data(std::move(value)), next(nullptr) {} // Konstruktor przenoszący
            };

            mynode* head;
            mynode* tail;
            int size;

        public:
            mylist(); // Konstruktor domyślny
            ~mylist(); // Destruktor
            mylist(std::initializer_list<T> init); // Konstruktor z listą inicjalizującą
            mylist(const mylist<T>& other); // Konstruktor kopiujący
            mylist(mylist<T>&& other); // Konstruktor przenoszący
            mylist<T>& operator=(const mylist<T>& other); // Przypisanie kopiujące
            mylist<T>& operator=(mylist<T>&& other); // Przypisanie przenoszące
            void clear(); // Czyszczenie zawartości listy
            void prepend(const T& value); // Wstawienie elementu na początek listy
            void append(const T& value); // Wstawienie elementu na koniec listy
            void insert(int idx, const T& value); // Wstawienie elementu na zadaną pozycję
            void pop(); // Usunięcie elementu z końca listy
            void pop(int idx); // Usunięcie elementu o określonej pozycji
            void remove(const T& value); // Usunięcie elementu o zadanej wartości
            void filter(const T& value); // Usunięcie wszystkich elementów o zadanej wartości
            int index(const T& value) const; // Określenie pozycji elementu o zadanej wartości
            int count(const T& value) const; // Policzenie wszystkich elementów o zadanej wartości
            int getSize() const; // Zliczenie wszystkich elementów na liście
            bool isEmpty() const; // Sprawdzenie czy lista jest pusta
            T getData(int idx) const; // Pobranie wartości
            friend std::ostream& operator<< <> (std::ostream& out, const mylist<T>& other); // Wypisywanie zawartości listy
    };

// Trait lessthan
template <typename T>
struct lessthan {
    bool operator()(const T& a, const T& b) const {
        return a < b;
    }
};

// Trait lessthan (specjalizacja: wskaźniki)
template <typename T>
struct lessthan<T*> {
    bool operator()(const T* a, const T* b) const {
        return *a < *b;
    }
};

// Trait lessthan (specjalizacja: const char*)
template <>
struct lessthan<const char*> {
    bool operator()(const char* a, const char* b) const {
        return std::strcmp(a, b) < 0;
    }
};

// Trait greaterthan
template <typename T>
struct greaterthan {
    bool operator()(const T& a, const T& b) const {
        return a > b;
    }
};

// Trait greaterthan (specjalizacja: wskaźniki)
template <typename T>
struct greaterthan<T*> {
    bool operator()(const T* a, const T* b) const {
        return *a > *b;
    }
};

// Trait greaterthan (specjalizacja: const char*)
template <>
struct greaterthan<const char*> {
    bool operator()(const char* a, const char* b) const {
        return std::strcmp(a, b) > 0;
    }
};

// Sprawdzanie czy lista jest uporządkowana
template <typename T, typename Compare = lessthan<T>>
bool issorted(const mylist<T>& list, Compare comp = Compare()) {
    if (list.isEmpty() || list.getSize == 1)
        return true;

    for (int i = 0; i < list.getSize() - 1; i++)
        if (!comp(list.getData(i), list.getData(i + 1)))
            return false;

    return true;
}

// Sortowanie elementów listy (sortowanie bąbelkowe)
template <typename T, typename Compare = lessthan<T>>
void sort(mylist<T>& list, Compare comp = Compare()) {
    int n = list.getSize();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            T a = list.getData(j);
            T b = list.getData(j + 1);
            if (!comp(a, b)) {
                list.pop(j);
                list.insert(j, b);
                list.pop(j + 1);
                list.insert(j + 1, a);
            }
        }
    }
}

}

#include "mylist.tpp"

#endif