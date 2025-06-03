CXX = g++
CXXFLAGS := $(CXXFLAGS) -Wall -std=c++23 -O2 -static

SRCS = main.cpp kolor.cpp kolortransparentny.cpp kolornazwany.cpp kolortransnaz.cpp piksel.cpp pikselkolorowy.cpp

TARGET = zadanie

all: $(TARGET)

$(TARGET): $(SRCS)
	$(CXX) $(CXXFLAGS) $(SRCS) -o $(TARGET)

clean:
	rm -f $(TARGET)

.PHONY: all clean
