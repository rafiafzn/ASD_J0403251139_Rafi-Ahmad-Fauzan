#5 Merge Sort Descending
def mergeSortDescending(data):
    if len(data) > 1:
        mid = len(data) // 2
        lefthalf = data[:mid]
        righthalf = data[mid:]
        mergeSortDescending(lefthalf)
        mergeSortDescending(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] >= righthalf[j]:
                data[k] = lefthalf[i]
                i = i + 1
            else:
                data[k] = righthalf[j]
                j = j + 1
            k = k + 1
        while i < len(lefthalf):
            data[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            data[k] = righthalf[j]
            j = j + 1
            k = k + 1

data_merge = [54,26,93,17,77,31,44,55,20]
mergeSortDescending(data_merge)
print("Merge Sort Descending:", data_merge)