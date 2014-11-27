CC = g++
CFLAGS = -c -Wall -Werror -std=c++11 $(DEBUG)
LDFLAGS = $(DEBUG)
EXE = a.out

SDIR = src
ODIR = obj

# matches all *.cpp files in $(SDIR)
FILES = $(patsubst $(SDIR)/%, %, $(wildcard $(SDIR)/*.cpp))

SOURCES = $(patsubst %, $(SDIR)/%, $(FILES))
OBJECTS = $(patsubst %, $(ODIR)/%, $(FILES:.cpp=.o))

all: $(EXE)

debug: all
debug: DEBUG = -D DEBUG -g

$(EXE): $(OBJECTS)
	@echo ""
	$(CC) $(LDFLAGS) $^ -o $@

$(ODIR)/%.o: $(SDIR)/%.cpp
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm -f $(OBJECTS) $(EXE)
	@echo ""

remake: clean all

test: all
	cat spreadsheet.txt | ./$(EXE)
