def spiralOrder(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return []
    else:
        ret = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        while top < bottom and left < right:
            for i in range(left, right):
                ret += [matrix[top][i]]
            for i in range(top, bottom):
                ret += [matrix[i][right]]
            for i in range(right, left, -1):
                ret += [matrix[bottom][i]]
            for i in range(bottom, top, -1):
                ret += [matrix[i][left]]
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        if top == bottom:
            for i in range(left, right + 1):
                ret += [matrix[top][i]]
        elif left == right:
            for i in range(top, bottom + 1):
                ret += [matrix[i][left]]
        return ret
print spiralOrder([[11, 12, 13, 14, 15],[21, 22, 23, 24, 25], [31, 32, 33, 34, 35], [41, 42, 43, 44, 45]])
Hi Morgan,

I am so excited to receive your email.

The following time works for me.
Monday 12/15, 4:00 PM - 7:00 PM CT
Tuesday 12/16, 8:00 AM - 7:00 PM CT
Wednesday 12/17 8:00 AM - 4:00 PM CT

Looking forward to speaking with you!

Regards,
Hao
