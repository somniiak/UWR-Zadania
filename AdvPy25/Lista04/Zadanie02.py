from itertools import product

class Formula:
    def __add__(self, other):
        return Or(self, other)

    def __mul__(self, other):
        return And(self, other)

    def oblicz(self, zmienne):
        raise NotImplementedError

    def zmienne(self):
        raise NotImplementedError
    
    def uprosc(self):
        return self

    def tautologia(self):
        zm = sorted(self.zmienne())
        return all(
            self.oblicz(dict(zip(zm, prod)))
            for prod in product(
                [False, True], repeat=len(zm)
            )
        )

class Stala(Formula):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "true" if self.value else "false"

    def oblicz(self, zmienne):
        return self.value

    def zmienne(self):
        return set()

class Zmienna(Formula):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def oblicz(self, zmienne):
        return zmienne[self.value]

    def zmienne(self):
        return {self.value}

class Not(Formula):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return ("¬" + str(self.value)
            if isinstance(self.value, (Stala, Zmienna))
            else f"({self.value})")

    def oblicz(self, zmienne):
        return not self.value.oblicz(zmienne)
    
    def zmienne(self):
        return self.value.zmienne()

    def uprosc(self):
        simplified = self.value.uprosc()

        # ¬true ≡ false
        # ¬false ∨ p ≡ true
        if isinstance(simplified, Stala):
            return Stala(not simplified.value)

        # ¬¬x ≡ x
        if isinstance(simplified, Not):
            return simplified.value

        return Not(simplified)

class Or(Formula):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        l = (str(self.left)
            if isinstance(self.left, (Stala, Zmienna, Not))
            else f"({self.left})")
        
        r = (str(self.right)
            if isinstance(self.right, (Stala, Zmienna, Not))
            else f"({self.right})")

        return l + " ∨ " + r

    def oblicz(self, zmienne):
        return self.left.oblicz(zmienne) or self.right.oblicz(zmienne)

    def zmienne(self):
        return self.left.zmienne() | self.right.zmienne()

    def uprosc(self):
        l = self.left.uprosc()
        r = self.right.uprosc()

        # true ∨ p ≡ true
        # p ∨ true ≡ true
        if isinstance(l, Stala) and l.value:
            return Stala(True)
        if isinstance(r, Stala) and r.value:
            return Stala(True)

        # false ∨ p ≡ p
        # p ∨ false ≡ p
        if isinstance(l, Stala) and not l.value:
            return r
        if isinstance(r, Stala) and not r.value:
            return l

        return Or(l, r)

class And(Formula):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        l = (str(self.left)
            if isinstance(self.left, (Stala, Zmienna, Not))
            else f"({self.left})")

        r = (str(self.right)
            if isinstance(self.right, (Stala, Zmienna, Not))
            else f"({self.right})")

        return l + " ∧ " + r

    def oblicz(self, zmienne):
        return self.left.oblicz(zmienne) and self.right.oblicz(zmienne)

    def zmienne(self):
        return self.left.zmienne() | self.right.zmienne()

    def uprosc(self):
        l = self.left.uprosc()
        r = self.right.uprosc()

        # false ∧ p ≡ false
        # p ∧ false ≡ false
        if isinstance(l, Stala) and not l.value:
            return Stala(False)
        if isinstance(r, Stala) and not r.value:
            return Stala(False)

        # true ∧ p ≡ p
        # p ∧ true ≡ p
        if isinstance(l, Stala) and l.value:
            return r
        if isinstance(r, Stala) and r.value:
            return l

        return And(l, r)



f = Or(Not(Zmienna("x")), And(Zmienna("y"), Stala(True)))
print(f)
print(f.zmienne())
print(f.tautologia())
print(f.oblicz({"x": False, "y": True}))
print(f.uprosc())