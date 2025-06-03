#ifndef OPERATOR2_H
#define OPERATOR2_H

#include "operator1.hpp"

namespace obliczenia
{
    class operator2 : public operator1
    {
        protected:
            wyrazenie* arg2;

        public:
            operator2(wyrazenie* a, wyrazenie* b);
            virtual ~operator2();
    };
}
#endif
