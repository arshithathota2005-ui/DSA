#peek and delete

stack = []
n = int(input("Eneter the size"))
for i in range(n):
    val = int(input("Enter the element"))
    stack.append(val)
print("Stack:",stack)
print("Peek:",stack[-1])
if len(stack)==0:
    print("Stack is empty")
else:
    print("delete element",stack.pop())
print("stack:",stack)
