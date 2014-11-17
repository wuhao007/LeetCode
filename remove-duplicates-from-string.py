def remove_dup(S):
    st = set([])
    ret = ''
    for s in S:
        if s not in st:
            ret += s
            st.add(s)
    return ret
print remove_dup("aaaabbcccdddw")            

