#bruteforce approach
'''arr = list(map(int,input().split()))
t = int(input())
c = 0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] ==t:
            print(arr[i],arr[j])
            c+=1
'''

