#4 Shell Sort Descending
def gapInsertionSortDescending(data, start, gap):
    for i in range(start + gap, len(data), gap):
        currentvalue = data[i]
        position = i
        while position >= gap and data[position - gap] < currentvalue:
            data[position] = data[position - gap]
            position = position - gap
        data[position] = currentvalue

def shellSortDescending(data):
    sublistcount = len(data) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSortDescending(data, startposition, sublistcount)
        sublistcount = sublistcount // 2

data_shell = [54,26,93,17,77,31,44,55,20]
shellSortDescending(data_shell)
print("Shell Sort Descending:", data_shell)
