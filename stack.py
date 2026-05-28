stack = []
size = 5

def push(item):
    if len(stack) == size:
        print("stack is full")
    else:
        stack.append(item)
        print("item pushed", item)

def pop():
    if len(stack) == 0:
        print("stack is empty")
    else:
        remove = stack.pop()
        print("item popped", remove)
def peek():
    if len(stack) == 0:
        print("stack is empty")
    else:
        print("item peeked is",stack[-1])
def isEmpty():
    if len(stack) == 0:
        print("stack is empty")
    else:
        print("stack is not empty")
def isFull():
    if len(stack) == size:
        print("stack is full")
    else:
        print("stack is not full")

push(1)
push(2)
print(stack)
peek()
pop()
pop()
pop()

