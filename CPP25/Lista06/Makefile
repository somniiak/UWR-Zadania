CXX = g++
CXXFLAGS := $(CXXFLAGS) -Wall -std=c++23 -O2

SRCS = main.cpp
TARGET = zadanie

LIB_COMPLEX = libcomplex.so
LIBSRC_COMPLEX = complex.cpp

LIB_POLYNOMINAL = libpolynominal.so
LIBSRC_POLYNOMINAL = polynominal.cpp

all: $(LIB_COMPLEX) $(LIB_POLYNOMINAL) $(TARGET)
lib: $(LIB_COMPLEX) $(LIB_POLYNOMINAL)

# Kompilacja bibliotek łączonych dynamicznie:
# -fPIC (Position Independent Code): tworzy kod niezależny od
# konkretnego adresu w pamięci (wymagane dla bibliotek współdzielonych)
# -shared: tworzy bibliotekę współdzieloną (.so), a nie plik wykonywalny
$(LIB_COMPLEX): $(LIBSRC_COMPLEX)
	$(CXX) -fPIC -shared -o $(LIB_COMPLEX) $(LIBSRC_COMPLEX)

$(LIB_POLYNOMINAL): $(LIBSRC_POLYNOMINAL)
	$(CXX) -fPIC -shared -o $(LIB_POLYNOMINAL) $(LIBSRC_POLYNOMINAL)

# -L.: gdzie szukać biblioteki ("." - bieżący folder)
# -lcomplex: dołącza bibliotekę libcomplex.so
# (ogólnie -lXYZ dołącza libXYZ.so lub libXYZ.a)
# Aby uruchomić program trzeba wczytać bibliotekę ustawiając
# zmienną środowiskową: export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH
# (gdzie "." to oczywiście bieżący katalog).
# Można też ustawić ścieżkę do biblioteki w trakcie linkowania,
# używając flagi -rpath w trakcie kompilacji.
# -Wl,-rpath=. powoduje, że w pliku wykonywalnym zapisuje się
# ścieżka do katalogu, w którym znajduje się biblioteka.
$(TARGET): $(SRCS)
	$(CXX) $(CXXFLAGS) $(SRCS) -L. -lcomplex -lpolynominal -Wl,-rpath=. -o $(TARGET)

clean:
	rm -f $(TARGET) $(LIB_COMPLEX) $(LIB_POLYNOMINAL)

.PHONY: all clean
