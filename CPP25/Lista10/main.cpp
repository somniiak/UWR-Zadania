#include <iostream>

#include "mylist.hpp"
#include "myqueue.hpp"
#include "mystack.hpp"

using namespace adt;

int main()
{
    std::cout << "myCharList:" << std::endl;
    mylist<char> myCharList = {'g', 'R', 't', 'f', 'h', 'p', 'a', 'Q', 'P'};
    myCharList.append('b');
    myCharList.prepend('o');
    myCharList.insert(5, 'A');
    std::cout << myCharList << std::endl;
    sort(myCharList);
    std::cout << myCharList << std::endl;
    std::cout << "Rozmiar: " << myCharList.getSize() << std::endl;
    std::cout << "Lista pusta: " << myCharList.isEmpty() << std::endl;
    myCharList.prepend('A');
    myCharList.prepend('A');
    myCharList.prepend('A');
    myCharList.append('A');
    myCharList.append('A');
    std::cout << myCharList << std::endl;
    std::cout << "Usuwanie 'A'..." << std::endl;
    myCharList.filter('A');
    std::cout << myCharList << std::endl;

    std::cout << "myIntStack:" << std::endl;
    mystack<int> myIntStack;
    myIntStack.push(1);
    std::cout << myIntStack << std::endl;
    myIntStack.push(2);
    std::cout << myIntStack << std::endl;
    myIntStack.push(3);
    std::cout << myIntStack << std::endl;
    int item1 = myIntStack.take();
    std::cout << myIntStack << "; Zabrano " << item1 << std::endl;
    int item2 = myIntStack.take();
    std::cout << myIntStack << "; Zabrano " << item2 << std::endl;
    int item3 = myIntStack.take();
    std::cout << myIntStack << "; Zabrano " << item3 << std::endl;
    // Pobieranie elementu z pustego stosu
    // myIntStack.take();

    return 0;
}
