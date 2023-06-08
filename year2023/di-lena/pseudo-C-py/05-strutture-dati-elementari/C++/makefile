#commands
CC = g++
CFLAGS = -Wall -g -std=c++11
LINK = g++

#folders
SRC_DIR := ./src/
OBJ_DIR := ./build/
SRC_FILES := $(wildcard $(SRC_DIR)*.cpp)
OBJ_FILES := $(patsubst $(SRC_DIR)%.cpp,$(OBJ_DIR)%.o,$(SRC_FILES))

app: $(OBJ_FILES)
	$(LINK) -o $@ $^

#main should be recompiled when i have templates types
TEMPLATES := $(SRC_FILES)

$(OBJ_DIR)main.o: $(SRC_DIR)main.cpp $(TEMPLATES)
	mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

$(OBJ_DIR)%.o: $(SRC_DIR)%.cpp
	mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(OBJ_DIR) app
