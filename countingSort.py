def countingSort(arr):
    frequency_array = [0]*100
    for i in arr:
        frequency_array[i] += 1
    return frequency_array