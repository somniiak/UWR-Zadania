CXX = g++
CXXFLAGS := -Wall -std=c++23 -O3 -static \
	-I. -Iop-bin -Iop-rel -Iop-unr -Ioperands

SRCS = $(wildcard *.cpp) \
	$(wildcard op-bin/*.cpp) \
	$(wildcard op-rel/*.cpp) \
	$(wildcard op-unr/*.cpp) \
	$(wildcard operands/*.cpp)

TARGET = zadanie

all: $(TARGET)

$(TARGET): $(SRCS)
	$(CXX) $(CXXFLAGS) $(SRCS) -o $(TARGET)

clean:
	rm -f $(TARGET)

.PHONY: all clean
