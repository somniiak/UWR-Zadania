# Compiler and flags
CXX = g++
CXXFLAGS = -Wall -std=c++11 -O2 -static

# Source files
SRCS = main.cpp circle.cpp point.cpp vector.cpp line.cpp

# Output executable
TARGET = zadanie

# Default rule: build the target
all: $(TARGET)

# Rule to compile and link the source files directly into the executable
$(TARGET): $(SRCS)
	$(CXX) $(CXXFLAGS) $(SRCS) -o $(TARGET)

# Clean up generated files
clean:
	rm -f $(TARGET)

# Phony targets
.PHONY: all clean
