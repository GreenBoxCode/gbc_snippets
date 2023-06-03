# Compiler and flags
CXX        := g++
CXXFLAGS   := -Wall -Wextra -O3 -std=c++20
DEBUGFLAGS := -g -DDEBUG
LDFLAGS    := -L/usr/lib -L./libs -lstdc++ -lm
LDLIBS     :=

# Directories
SRC_DIR   := src
HDR_DIR   := hdr
OBJ_DIR   := build/objects
BIN_DIR   := build/bin
DEP_DIR   := build/dependencies

# Targets
PROJECT_NAME := $(notdir $(shell pwd))
TARGET       := $(BIN_DIR)/$(PROJECT_NAME)
SRC_FILES    := $(wildcard $(SRC_DIR)/*.cpp)
OBJ_FILES    := $(patsubst $(SRC_DIR)/%.cpp,$(OBJ_DIR)/%.o,$(SRC_FILES))
DEP_FILES    := $(patsubst $(SRC_DIR)/%.cpp,$(DEP_DIR)/%.d,$(SRC_FILES))

# Phony targets
.PHONY: all clean debug

# Default target
all: $(TARGET)

# Create directories
$(OBJ_DIR) $(BIN_DIR) $(DEP_DIR):
	mkdir -p $@

# Build object files
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp | $(OBJ_DIR) $(DEP_DIR)
	$(CXX) $(CXXFLAGS) -c -MMD -MP -MF $(patsubst $(OBJ_DIR)/%.o,$(DEP_DIR)/%.d,$@) -o $@ $<

# Build the final executable
$(TARGET): $(OBJ_FILES) | $(BIN_DIR)
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $^ $(LDLIBS)

# Include dependency files
-include $(DEP_FILES)

# Debug target
debug: CXXFLAGS += $(DEBUGFLAGS)
debug: all

# Clean build artifacts
clean:
	$(RM) -r $(OBJ_DIR) $(BIN_DIR) $(DEP_DIR)
