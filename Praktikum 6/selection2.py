#2 Selection Sort Descending
def selectionSortDescending(data):
    for i in range(len(data)):
        max_idx = i
        for j in range(i+1, len(data)):
            if data[j] > data[max_idx]:
                max_idx = j
        # Swap
        data[i], data[max_idx] = data[max_idx], data[i]

data = [54,26,93,17,77,31,44,55,20]
selectionSortDescending(data)
print("Selection Sort Descending:", data)