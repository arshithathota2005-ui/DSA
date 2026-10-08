#write a program to add sum of digits of a number

n = int(input())
s=0
while n!=0:
    d = n%10
    s = s+d
    n//=10
print(s)





