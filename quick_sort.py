def quicksort(arr):
    n = len(arr)
    if n<=1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x<=pivot]
    right = [x for x in arr[:-1] if x >pivot]
    return quicksort(left)+[pivot]+quicksort(right)
arr = list(map(int,input().split()))
print("sorted array",quicksort(arr))
