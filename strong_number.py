#Strong number

'''n = int(input())
s=0
t=n
while n!=0:
    d = n%10
    f =1
    for i  in range(1,d+1):
        f =f*i
    s+=f
    n//=10
if s ==t:
    print(t,"is strong number")
else:
    print(t,"is not a strong number")'''


#1/2!+2/3!+3/4!+............n
'''n = int(input())
s=0
f=1
for i in range(1,n+1):
    #f=1
    #for j in range(1,i):
    f = f*(i+1)
    s=s+(i/f)     
print(s)'''





