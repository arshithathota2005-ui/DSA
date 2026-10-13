#direct recursion -  numbers

def num(n):
    if n==0:
        return
    print(n)
    num(n-1)
n = int(input())
num(n)


#direct recursion - factorial of a numbers[= 

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
n = int(input())
print("Factorial :",fact(n))
