class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        automata = {
        (0, ' '):0, 

        (0, '-'):7, 
        (0, '+'):7, 

        (7, '.'):5, 
        (7, '0'):1, 
        (7, '1'):1, 
        (7, '2'):1, 
        (7, '3'):1, 
        (7, '4'):1, 
        (7, '5'):1, 
        (7, '6'):1, 
        (7, '7'):1, 
        (7, '8'):1, 
        (7, '9'):1, 

        (0, '.'):5, 
        (5, '0'):3, 
        (5, '1'):3, 
        (5, '2'):3, 
        (5, '3'):3, 
        (5, '4'):3, 
        (5, '5'):3, 
        (5, '6'):3, 
        (5, '7'):3, 
        (5, '8'):3, 
        (5, '9'):3, 

        (0, '0'):1, 
        (0, '1'):1, 
        (0, '2'):1, 
        (0, '3'):1, 
        (0, '4'):1, 
        (0, '5'):1, 
        (0, '6'):1, 
        (0, '7'):1, 
        (0, '8'):1, 
        (0, '9'):1, 

        (1, '0'):1, 
        (1, '1'):1, 
        (1, '2'):1, 
        (1, '3'):1, 
        (1, '4'):1, 
        (1, '5'):1, 
        (1, '6'):1, 
        (1, '7'):1, 
        (1, '8'):1, 
        (1, '9'):1, 

        (1, ' '):4, 
        (4, ' '):4, 

        (1, '.'):2, 
        (1, 'e'):6, 
        (6, '+'):9,
        (6, '-'):9,
        (9, '0'):8, 
        (9, '1'):8, 
        (9, '2'):8, 
        (9, '3'):8, 
        (9, '4'):8, 
        (9, '5'):8, 
        (9, '6'):8, 
        (9, '7'):8, 
        (9, '8'):8, 
        (9, '9'):8,

        (6, '0'):8, 
        (6, '1'):8, 
        (6, '2'):8, 
        (6, '3'):8, 
        (6, '4'):8, 
        (6, '5'):8, 
        (6, '6'):8, 
        (6, '7'):8, 
        (6, '8'):8, 
        (6, '9'):8,


        (2, '0'):3, 
        (2, '1'):3, 
        (2, '2'):3, 
        (2, '3'):3, 
        (2, '4'):3, 
        (2, '5'):3, 
        (2, '6'):3, 
        (2, '7'):3, 
        (2, '8'):3, 
        (2, '9'):3,
        (2, ' '):4,
        (2, 'e'):6,

        (3, '0'):3, 
        (3, '1'):3, 
        (3, '2'):3, 
        (3, '3'):3, 
        (3, '4'):3, 
        (3, '5'):3, 
        (3, '6'):3, 
        (3, '7'):3, 
        (3, '8'):3, 
        (3, '9'):3, 
        (3, 'e'):6, 
        (3, ' '):4,

        (8, '0'):8, 
        (8, '1'):8, 
        (8, '2'):8, 
        (8, '3'):8, 
        (8, '4'):8, 
        (8, '5'):8, 
        (8, '6'):8, 
        (8, '7'):8, 
        (8, '8'):8, 
        (8, '9'):8, 
        (8, ' '):4
        }
        def isNumber(state, s, automata):
            if s == '':
                return state == 1 or state == 8 or state == 2 or state == 3 or state == 4
            elif (state, s[0]) in automata:
                return isNumber(automata[(state, s[0])], s[1:], automata)
            else:
                return False
        return isNumber(0, s, automata)
solution = Solution()
print solution.isNumber("0") == True
print solution.isNumber(" 0.1 ") == True
print solution.isNumber("abc") == False
print solution.isNumber("1 a") == False
print solution.isNumber("2e10") == True
print solution.isNumber(".1") == True
print solution.isNumber(".") == False
print solution.isNumber("3.") == True
print solution.isNumber("0e") == False
print solution.isNumber("3. ") == True
print solution.isNumber("-1.") == True
print solution.isNumber("+.8") == True
print solution.isNumber(" -.") == False
print solution.isNumber("46.e3") == True
print solution.isNumber(".2e81") == True
print solution.isNumber("92e1740e91") == False
print solution.isNumber(" 005047e+6") == True
