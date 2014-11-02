_end = '_end_'
def make_trie(*words):
    root = {}
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict.setdefault(_end, _end)
    return root

def in_trie(trie, word):
    if type(trie) is not dict:
        return False
    elif len(word) == 0:
        return _end in trie
    else:
        if word[0] in trie:
            return in_trie(trie[word[0]], word[1:])
        elif word[0] == '*':
            for v in trie.values():
                if in_trie(v, word[1:]):
                    return True
            else:   
                return False

print in_trie(make_trie("new", "york", "univ", "univer", "ne"), 'ne')
print in_trie(make_trie("new", "york", "univ", "univer", "ne"), 'yo')
print in_trie(make_trie("new", "york", "univ", "univer", "ne"), 'u***')
print in_trie(make_trie("new", "york", "univ", "univer", "ne"), 'n*w')
print in_trie(make_trie("new", "york", "univ", "univer", "ne"), '*e')
print in_trie(make_trie("new", "york", "univ", "univer", "ne"), 'n****')
print in_trie(make_trie("new", "york", "univ", "univer", "ne"), 'y**l')
print in_trie(make_trie("new", "york", "univ", "univer", "ne"), '****')
