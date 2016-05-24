class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        longest = 0
        st = []
        for i in range(n):
            if s[i] == '(':
                st.append(i)
            else:
                if st:
                    if st[st[-1]] == '(':
                        st.pop()
                    else:
                        st.append(i)
                else:
                    st.append(i)

        if st:
            a, b = n, 0
            while st:
                b = st.pop()
                longest = max(longest, a - b - 1)
                a = b
            longest = max(longest, a)
        else:
            longest = n
        return longest
