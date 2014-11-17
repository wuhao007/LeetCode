def remove(s, pos):
    while pos + 1 < len(s):
        if s[pos] == s[pos+1]:
            s = s[:pos] + s[pos+2:]
            pos -= 1 if pos > 0 else 0
        else:
            pos += 1
    return s if len(s) > 0 else -1
print remove("ABCCBCBA", 0)
print remove("AA", 0)

