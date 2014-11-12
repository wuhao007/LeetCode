def remove_dup(S):
    st = set([])
    for s in S:
        st.add(s)
    ret = ''
    for s in S:
        if s in st:
            ret += s
            st.remove(s)
    return ret
print remove_dup("aaaabbcccdddw")            

