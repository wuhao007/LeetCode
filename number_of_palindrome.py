def getIsPalindrome(s):
    n = len(s)
    isPalindrome = [[False] * n for _ in range(n)]
   
    count = 0
    for i in range(n):
        isPalindrome[i][i] = True;
        count += 1

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            isPalindrome[i][i + 1] = True
            count += 1

    for length in range(2, n):
        for start in range(n - length):
            if isPalindrome[start + 1][start + length - 1] and s[start] == s[start + length]:
                isPalindrome[start][start + length] = True
                count += 1

    return count
print getIsPalindrome('aba')
print getIsPalindrome('abba')
