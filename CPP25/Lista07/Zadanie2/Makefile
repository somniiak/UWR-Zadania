CXX = g++
CXXFLAGS = -Wall -std=c++23 -O2 -static

TARGET = zadanie
SRCS = main.cpp $(wildcard instr-pod/*.cpp) $(wildcard instr-stk/*.cpp)

LIB_WYRAZENIE = libwyrazenie.a
LIBSRC_WYRAZENIE = $(wildcard wyrazenie/*.cpp) \
	$(wildcard wyrazenie/op-bin/*.cpp) \
	$(wildcard wyrazenie/op-rel/*.cpp) \
    $(wildcard wyrazenie/op-unr/*.cpp) \
	$(wildcard wyrazenie/operands/*.cpp)
LIBOBJ_WYRAZENIE = $(LIBSRC_WYRAZENIE:.cpp=.o)

LIB_WYRAZENIE_INCLUDES = -Iwyrazenie -Iwyrazenie/op-bin -Iwyrazenie/op-rel \
	-Iwyrazenie/op-unr -Iwyrazenie/operands
INCLUDES = $(LIB_WYRAZENIE_INCLUDES) -I. -Iinstr-pod -Iinstr-stk

all: $(TARGET)
lib: $(LIB_WYRAZENIE)

$(LIB_WYRAZENIE): $(LIBOBJ_WYRAZENIE)
	ar rcs $(LIB_WYRAZENIE) $(LIBOBJ_WYRAZENIE)

$(TARGET): $(SRCS) $(LIB_WYRAZENIE)
	$(CXX) $(CXXFLAGS) $(INCLUDES) $(SRCS) $(LIB_WYRAZENIE) -o $(TARGET)

# Reguła kompilowania .cpp -> .o
%.o: %.cpp
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

clean:
	rm -f $(TARGET) $(LIB_WYRAZENIE) $(LIBOBJ_WYRAZENIE)

.PHONY: all clean lib
