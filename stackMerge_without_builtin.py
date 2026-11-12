#merge 2 stacks with out built in method

stack1 = []
stack2 = []
stack3=[]
n = int(input("Enter the no of elements"))
for i in range(n):
    val = int(input("Enter a value:"))
    stack1.append(val)

print("Stack:",stack1)
for i in range(n):
    val = int(input("Enter a value"))
    stack2.append(val)

i, j = 0,0
while i<len(stack1) and j<len(stack2):
    if stack1[i]<stack2[j]:
        stack3.append(stack1[i])
        i+=1
    else:
        stack3.append(stack2[j])
        j+=1



print("Merged stack:",stack3)
