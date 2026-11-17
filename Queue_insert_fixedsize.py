#insert elements in a fixed queue
from queue import Queue
q = Queue(3)
n = int(input("Enter number of elements:"))
for i in range(n):
    val = int(input("Enter value"))
    if not q.full():
        q.put(val)
    else:
        print("Queue is full")
if q.full():
    print("Queue is full")
print("Queue",list(q.queue))
