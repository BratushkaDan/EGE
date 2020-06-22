arr = [5, 4, 3, 8, 1, 15]
for i in range(len(arr)):
    for k in range(len(arr)-i-1):
        if arr[k] > arr[k+1]:
            arr[k], arr[k + 1] = arr[k+1], arr[k]
print(arr)
