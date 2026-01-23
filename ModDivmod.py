# Enter your code here. Read input from STDIN. Print output to STDOUT
a  = int (input())
b = int (input())
def DivMod(a,b):
    print(a // b)
    print(a % b)
    print((a//b,a%b))
       
DivMod(a,b)