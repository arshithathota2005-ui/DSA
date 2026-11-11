#push operation till overflow
stack = []
size = int(input("Enter the size"))
n = int(input("Enter number of elements"))
for i in range(n):
    val = int(input("Enter the element"))
    if len(stack) == size:
        print("Stack Overflow")
    else:
        stack.append(val)
        print(val,"inserted")

print(stack,"stack")
        
