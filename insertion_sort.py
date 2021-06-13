def InsertionSort(arr):
    for i in range(arr.length):
        j= i-1
        temp = arr[i]

    while(j >= 0 and temp < arr[j]):
        arr[j + 1] = arr[j]
        j = j - 1
        
      arr[j + 1] = temp
