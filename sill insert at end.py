#insert at the end delete at begining
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = None
n = int(input())
for i in range(n):
    data = int(input())
    newnode = node(data)
    if head is None:
        head = newnode
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = newnode
print("SILL: before delete")
temp = head
while temp:
    print(temp.data,end="->")
    temp = temp.next
print("Tail")
#delete at beginning
if head is None:
    print("SILL is empty")
else:
    head = head.next

print("SILL after delete:")
temp = head
while temp:
    print(temp.data,end="->")
    temp = temp.next
print('Tail')
