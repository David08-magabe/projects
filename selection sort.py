def selection_sort(array):
    n = len(array)
    for ind in range(n-1):
        min_index = ind
        for j in range(ind+1,n):
            if array[j] < array[min_index]:
                min_index = j
        if ind!=min_index:
            array[ind],array[min_index] = array[min_index],array[ind]
array = [-2,45,0,11,-9,88,-97,-202,74]
selection_sort(array)
print(array)