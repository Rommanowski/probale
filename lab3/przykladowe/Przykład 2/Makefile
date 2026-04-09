CC=g++
CFLAGS=-m32 -Wall
ODIR=obj

ASM=nasm
ASMFLAGS=-f elf32

all: main.out funcs.so

$(ODIR)/main.o: main.cpp
	$(CC) -c -o $@ main.cpp $(CFLAGS)

$(ODIR)/funcs.o: funcs.asm
	$(ASM) $(ASMFLAGS) -o $@ funcs.asm

funcs.so: $(ODIR)/funcs.o
	$(CC) -fPIC -shared -o $@ $^ $(CFLAGS)

main.out: $(ODIR)/main.o $(ODIR)/funcs.o
	$(CC) -o $@ $(CFLAGS) $^

run: main.out
	./main.out

clean:
	rm -f $(ODIR)/*

.PHONY: all run clean