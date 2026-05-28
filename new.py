# def factorial(n):
#   #  if n==0 or n==1:
#        # return 1
#     result = 1
#     for i in range(1,n+1):
#         result *= i
#     return result
# print(factorial(1))

from collections import deque
queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

queue.popleft()
print(queue)

