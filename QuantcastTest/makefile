CC = g++
CFLAGS = -c -Wall -Werror -std=c++03 $(DEBUG)
LDFLAGS = $(DEBUG)
EXE = a.out

SDIR = src
ODIR = obj

FILES = $(patsubst $(SDIR)/%, %, $(wildcard $(SDIR)/*.cpp))

SOURCES = $(patsubst %, $(SDIR)/%, $(FILES))
OBJECTS = $(patsubst %, $(ODIR)/%, $(FILES:.cpp=.o))

all: $(EXE)

$(EXE): $(OBJECTS)
	@echo ""
	$(CC) $(LDFLAGS) $^ -o $@

$(ODIR)/%.o: $(SDIR)/%.cpp
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm -f $(OBJECTS) $(EXE)
	@echo ""

test: all
	cat spreadsheet.txt | ./$(EXE)
