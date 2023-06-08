#commands
CC = g++
CFLAGS = -Wall -g -std=c++11
LINK = g++

#folders
SRC_DIR := ./src/
OBJ_DIR := ./build/
SRC_FILES := $(wildcard $(SRC_DIR)/*.cpp)
OBJ_FILES := $(patsubst $(SRC_DIR)/%.cpp,$(OBJ_DIR)/%.o,$(SRC_FILES))

app: $(OBJ_FILES)
#main should be recompiled or the result is the same...
	$(CC) $(CFLAGS) -c $(SRC_DIR)main.cpp -o $(OBJ_DIR)main.o
	$(LINK) -o $@ $^

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(OBJ_DIR) app
