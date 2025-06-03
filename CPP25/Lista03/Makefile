CXX = g++
CXXFLAGS = -Wall -std=c++23 -O2 -static

SRCS = main.cpp punkt.cpp kolejka.cpp

TARGET = zadanie

all: $(TARGET)

$(TARGET): $(SRCS)
	$(CXX) $(CXXFLAGS) $(SRCS) -o $(TARGET)

clean:
	rm -f $(TARGET)

.PHONY: all clean
