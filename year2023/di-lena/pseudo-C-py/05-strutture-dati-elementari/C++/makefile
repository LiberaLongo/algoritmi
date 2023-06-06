#commands
CC = g++
CFLAGS = -Wall -g

#folders
sd = ./struttura-dati/
build = ./build/
 
app: $(build)main.o $(build)Lista.o
	$(CC) $(CFLAGS) -o app $(build)main.o $(build)Lista.o
 
$(build)main.o: $(sd)main.cpp $(sd)Lista.hpp
	mkdir -p $(build)
	$(CC) $(CFLAGS) -o $(build)main.o -c $(sd)main.cpp

$(build)Lista.o: $(sd)Lista.hpp $(sd)Lista.cpp

clean:
	cd $(build)
	rm *.o app