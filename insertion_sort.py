arr = list(map(int,input().split()))
n = len(arr)
for i in range(n):
    x=arr[i]
    j = i-1
    while j>=0 and arr[j]>x:
        arr[j+1] = arr[j]
        j-=1
    arr[j+1]=x
print(*arr)
