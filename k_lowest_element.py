def FirstKelements(arr, k):
    size = len(arr)
    minHeap = []
    for i in range(k):
        minHeap.append(arr[i])

    for i in range(k, size):
        minHeap.sort()

        if minHeap[0] > arr[i]:
            continue

        else:
            minHeap.pop(0)
            minHeap.append(arr[i])

    for i in minHeap:
        print(i, end=" ")


arr = [11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45]
k = 3
FirstKelements(arr, k)
