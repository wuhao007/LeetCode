def _anagrams(A, B):
    if len(A) != len(B):
        return False
    hm = {}
    for a in A:
        if a in hm:
            hm[a] += 1
        else:
            hm[a] = 1
    for b in B:
        if b in hm:
            hm[b] -= 1
            if hm[b] == 0:
                hm.pop(b, None)
        else:
            return False
    return len(hm.keys()) == 0
def anagrams(A, B):
    if _anagrams(A, B):
        print 'Anagrams!'
    else:
        print 'Not anagrams!'
anagrams('', '')
anagrams('the eyes', 'they see')
anagrams('the eyes', 'they do see')
anagrams('the eyes', 'they see!')
anagrams('school master', 'the classroom')
anagrams('One sentence.', 'Another sentence.')
