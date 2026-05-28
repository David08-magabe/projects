from collections import deque
queue = deque()
size = 3

def enqueue(item):
    if len(queue) < size:
        queue.append(item)
        print(item,"added to queue")
    else:
        print("queue is full")

def dequeue():
    if len(queue) > 0:
        removed = queue.popleft()
        print(removed,"removed from queue")
    else:
        print("queue is empty")

enqueue(5)
enqueue(6)
enqueue(7)
enqueue(8)

print(queue)

dequeue()
dequeue()
dequeue()
dequeue()

print(queue)


