def print_bst(h):
    for level in range(h):
        number = 2 ** (h - level) - 1
        space = ' ' * (number / 2)
        line = ''
        for i in range(2 ** level):
            line += (space + ' *' + space)
        print line
print_bst(6)
