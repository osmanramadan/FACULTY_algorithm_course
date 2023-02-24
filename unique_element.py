def unique_element(arr):
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return False
    return True


arr = [0, 1, 2, 3, 3]
print(unique_element(arr))
