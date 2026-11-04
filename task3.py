def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
        
    if right < n and arr[right] > arr[largest]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)
    return arr


def heapsort_trace(arr):
    n = len(arr)
    print(f"original array: {arr}")
    
    iterations = []
    
    for i in range(n - 1, n - 3, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, i, 0)
        iterations.append(list(arr))
        
    return iterations

def heap_insert(heap, key):
    heap.append(key)
    i = len(heap) - 1
    
    while i > 0:
        parent = (i - 1) // 2
        if heap[i] > heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break
    return heap


arr5 = [3, 9, 2, 1, 4, 5]
result5 = build_max_heap(arr5)
print(f"Max-Heap: {result5}")

arr6 = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
trace_results = heapsort_trace(arr6)
print(f"Iteration 1: {trace_results[0]}")
print(f"Iteration 2: {trace_results[1]}")

heap7 = [16, 14, 10, 8, 7, 9, 3]
result7 = heap_insert(heap7, 15)
print(f"array after adding 15: {result7}")
