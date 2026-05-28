def binary_search(array,target):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = (low+high)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            high = mid - 1
        elif array[mid] < target:
            low = mid + 1
    return -1
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
target = int(input("Enter a number: "))
index = binary_search(array,target)
if index < 0:
    print(f"{target} is out of the range")
else:
    print(f"{target} found at index {index}")
