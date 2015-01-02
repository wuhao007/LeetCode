def sparse_vector_multiply(this, that):
    s = 0.0
    for i, value in this.items():
        if i in that:
            s += that[i] * value
    return s
this = {2:0.36,3:0.36,4:0.18}
that = {0:0.05, 1:0.04, 2:0.36, 3:0.37, 4:0.19}
print sparse_vector_multiply(this, that)

