#ifndef MYSTACK_HPP
#define MYSTACK_HPP

#include "mylist.hpp"

namespace adt
{
    template <typename T>
    class mystack : private mylist<T>
    {
        public:
            mystack(); // Konstruktor domyślny
            ~mystack(); // Destruktor
            mystack(std::initializer_list<T> init); // Konstruktor z listą inicjalizującą
            mystack(const mystack<T>& other); // Konstruktor kopiujący
            mystack(mystack<T>&& other); // Konstruktor przenoszący
            mystack<T>& operator=(const mystack<T>& other); // Przypisanie kopiujące
            mystack<T>& operator=(mystack<T>&& other); // Przypisanie przenoszące
            void push(const T& value); // Dodanie elementu na stos
            T take(); // Zabranie elementu ze stosu
            template <typename U>
            friend std::ostream& operator<<(std::ostream& out, const mystack<U>& other); // Wypisywanie zawartości listy
    };
}

#include "mystack.tpp"

#endif
