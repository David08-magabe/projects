def  bubble_sort(array):
    n = len(array)
    if n< 2:
        return array
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                swapped = True
        if not swapped:
           break
    return array
array = [2,0,7,9,10,11,4,6]
bubble_sort(array)
print(array)