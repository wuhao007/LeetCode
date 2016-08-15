def sortLetters(chars):
    # write your code here
    chars = list(chars)
    lo = 0
    i = 0
    gt = len(chars) - 1
    while i <= gt:
        print chars[i]
        if chars[i].isupper():
            print "upper"
            i += 1
        else:
            chars[lo], chars[i] = chars[lo], chars[i]
            lo += 1
            i += 1
    return chars
chars = "abAcD"
print sortLetters(chars)
