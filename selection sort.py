# buble sort implementation

a = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selectionSort(arr):
    if len(arr) == 1:
        return arr
    i = 0
    minNum = 0
    while i<len(arr)-1:
 
        for j in range(i,len(arr)):
            if arr[minNum] > arr[j]:
                minNum = j
        arr[i], arr[minNum] = arr[minNum], arr[i]
        
        i = i + 1
        
    return arr
             

print(selectionSort(a))


