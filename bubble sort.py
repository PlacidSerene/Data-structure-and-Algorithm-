# buble sort implementation

a = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubblesort(arr):
    i = len(arr) - 1
    while i > 0:
  
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
         
        i = i-1
    return arr

print(bubblesort(a))


