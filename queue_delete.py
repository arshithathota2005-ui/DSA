#delete of elements using queue
from queue import Queue
q = Queue()
n = int(input("Eneter number of elements"))
for i in range(n):
    val = int(input("Enter value:"))
    q.put(val)
while not q.empty():
    print(q.get(),":deleted")
print("Queue empty")
