#ifndef OPERATOR1_H
#define OPERATOR1_H

#include "wyrazenie.hpp"

namespace obliczenia
{
    class operator1 : public wyrazenie
    {
        protected:
            wyrazenie* arg1;

        public:
            operator1(wyrazenie* a);
            virtual ~operator1();
    };
}

#endif
