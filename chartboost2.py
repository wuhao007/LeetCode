from sys import stdin, stdout
userinput = stdin.readline()
string = userinput.split()
n = len(string)
for i in range(n/2):
    string[i], string[n-1-i] = string[n-1-i], string[i]
stdout.write(' '.join(string))
