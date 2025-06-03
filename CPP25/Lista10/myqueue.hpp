#ifndef MYQUEUE_HPP
#define MYQUEUE_HPP

#include "mylist.hpp"

namespace adt
{
    template <typename T>
    class myqueue : private mylist<T>
    {
        public:
            myqueue(); // Konstruktor domyślny
            ~myqueue(); // Destruktor
            myqueue(std::initializer_list<T> init); // Konstruktor z listą inicjalizującą
            myqueue(const myqueue<T>& other); // Konstruktor kopiujący
            myqueue(myqueue<T>&& other); // Konstruktor przenoszący
            myqueue<T>& operator=(const myqueue<T>& other); // Przypisanie kopiujące
            myqueue<T>& operator=(myqueue<T>&& other); // Przypisanie przenoszące
            void enqueue(const T& value); // Dodanie elementu na koniec kolejki
            T dequeue(); // Zabranie elementu z początku kolejki
            template <typename U>
            friend std::ostream& operator<<(std::ostream& out, const myqueue<U>& other); // Wypisywanie zawartości listy
    };
}

#include "myqueue.tpp"

#endif
