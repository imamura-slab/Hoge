TARGET = 
ifeq ($(TARGET), map.cpp)
	VERSION = c++17
else
	VERSION = c++11
endif 

all: $(TARGET)
	g++ -std=$(VERSION) $(TARGET) -g && ./a.out

clean:
	rm -rf *~ ./a.out
