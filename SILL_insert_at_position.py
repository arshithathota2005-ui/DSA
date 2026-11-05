#insert at position 
class node:
    def __init__(self,data):
        self.data= data
        self.next= None 
head = None 
n = int(input("Enter number of nodes : "))
for i in range(n):
    data = int(input("Enter a value : "))
    newnode = node(data)
    newnode.next = head
    head= newnode
print("SLL: before insert: ")
temp= head 
while temp:
    print(temp.data, end= '->')
    temp= temp.next 
print("Tail")
pos= int(input("Enter the position :"))
data = int(input("enter the data "))
newnode= node(data)
if pos==1 :
    newnode.next= head 
    head= newnode 
else:
    temp= head 
    count= 1 
    while temp and count <pos-1 :
        temp= temp.next 
        count+=1 
    if temp is None :
        print("Invalid position")
    else:
        newnode.next= temp.next 
        temp.next = newnode 
print("SLL: after insert: ")
temp= head 
while temp:
    print(temp.data, end= '->')
    temp= temp.next 
print("Tail")
