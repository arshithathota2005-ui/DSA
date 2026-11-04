#SLL insertr from begining
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = None

n = int(input())
for i in range(n):
    data = int(input())
    newnode = node(data)
    newnode.next = head
    head = newnode

print("SIL:")
temp = head
while temp:
    print(temp.data,end="->")
    temp = temp.next

print("Tail")
