def number_of_k(n, k):
    if n > 0:
        a = n % 10
        b = n / 10

        c = 1
        if b > 9 or b % 10 > k:
            c = 10
        else:
            c = a + 1
        if a >= k:
            b += 1
        
        print a,b,c
        
        return b + c * number_of_k(b, k)
    else:
        return 0

print number_of_k(302, 2)
