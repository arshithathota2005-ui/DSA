#push operation and merge 2 stacks 1 3 5 -2 4 6 1 2  3 4 5 6

stack1 = []
stack2 = []
n = int(input("Enter the no of elements"))
for i in range(n):
    val = int(input("Enter a value:"))
    stack1.append(val)

print("Stack:",stack1)
for i in range(n):
    val = int(input("Enter a value"))
    stack2.append(val)

print("Stack2:",stack2)
stack1.extend(stack2)
stack1.sort()
print(stack1)
