#indirect recursion
'''def one(n):
    if n<=0:
        return
    print("One :",n)
    two(n-1)
def two(n):
    if n<=0:
        return
    print("Two :",n)
    one(n-1)
n = int(input())
one(n)'''



#print odd or even  without using %
def even(n):
    if n==0:
        print(c,"is even")
        return
    odd(n-1)
def odd(n):
    if n==0:
        print(c,"is odd")
        return
    even(n-1)
n = int(input())
c =n
even(n)
