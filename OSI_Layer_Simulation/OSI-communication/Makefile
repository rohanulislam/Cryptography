CC = gcc
CFLAGS = -Wall -Wextra

TARGET = osi

all: $(TARGET)

$(TARGET): main.c layers.c layers.h
	$(CC) $(CFLAGS) main.c layers.c -o $(TARGET)

clean:
	rm -f $(TARGET) *.o