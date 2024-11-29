# Makefile to compile a C program with 32-bit architecture and no stack protection

CC = gcc
CFLAGS = -m32 -g -fno-stack-protector -fno-stack-check -no-pie -z noexecstack -Wno-implicit-function-declaration

SRC = ret2win.c
OUT = ret2win

# Default target
all: $(OUT)

# Rule to compile and link the program
$(OUT): $(SRC)
	$(CC) $(CFLAGS) -o $(OUT) $(SRC)

# Clean target to remove generated files
clean:
	rm -f $(OUT)
