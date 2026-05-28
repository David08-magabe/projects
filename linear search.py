def linear_search(array,target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1
array = [10,20,30,40,50]
target = int(input("Enter your target: "))
index = linear_search(array,target)
if index < 0:
    print(f"{target} not found")
else:
    print(f"{target} is at {index} index")
