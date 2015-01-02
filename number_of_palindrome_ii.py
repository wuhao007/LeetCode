def getIsPalindrome(s):
    n = len(s)
    isPalindrome = [[0] * n for _ in range(n)]
   
    for i in range(n):
        isPalindrome[i][i] = 1;

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            isPalindrome[i][i + 1] = 3

    for length in range(2, n):
        for start in range(n - length):
            if isPalindrome[start + 1][start + length - 1] > 0 and s[start] == s[start + length]:
                isPalindrome[start][start + length] = isPalindrome[start + 1][start + length - 1] + 1

    return isPalindrome[0][n - 1]
print getIsPalindrome('aba')
print getIsPalindrome('abba')

