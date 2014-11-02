def appendsums(sum_three, iter):
    if len(sum_three) == iter + 1:
        return sum_three[-1]
    else:
        return appendsums (sum_three + [sum_three[-1] + sum_three[-2] + sum_three[-3]], iter)
print appendsums([0,1,2], 20) 
