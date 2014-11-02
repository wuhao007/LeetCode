string = "appleE"
hs = {}
for s in string:
    if s in hs:
        hs[s] += 1
    else:
        hs[s] = 1
for s in sorted(hs.keys()):
    if hs[s] is 1:
        print s, hs[s]
