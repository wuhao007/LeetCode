def gene_search(genome, gene):

    gene = list(gene)

    shifts = [1] * (len(gene) + 1)
    shift = 1
    for pos in xrange(len(gene)):
        while shift <= pos and gene[pos] != gene[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift

    startPos, matchLen = 0, 0
    for c in genome:
        while matchLen == len(gene) or matchLen >= 0 and gene[matchLen] != c:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == len(gene):
            return True
    return False    

print gene_search("ACCATGCA", "CAT") == True
print gene_search("CATTGA", "CAT") == True
print gene_search("GGCACACATG", "CACAT") == True
print gene_search("CAAAT", "CAT") == False
