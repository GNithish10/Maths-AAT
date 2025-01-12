import time
import numpy as np
def bubbleSort(arr):
    t0 = time.time()
    n = len(arr)
    
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break
    t1 = time.time()
    return (t1 - t0)


for i in range(100):
    arr = np.random.randint(1, 1000000, size=(1000))
    t=bubbleSort(arr)
    with open("Bubble-Out.txt", "a") as f:
        f.write(str(t)+"\n")
    
