# TejasOpenSource

def selectionSort(arrToBeSorted):
    toBeSwitched = None
    # For each element in array to be sorted, loop through array and see what minimum value is after that element
    for i in range(len(arrToBeSorted)):
        minNum = i  # Update minNum to be i so that we start at ith element
        for j in range(i+1, len(arrToBeSorted)):
            if (arrToBeSorted[j] < arrToBeSorted[minNum]):
                minNum = j

        # Get current element at position that min needs to be switched to
        toBeSwitched = arrToBeSorted[i]
        # Move min num to correct pos (e.g. second smallest number would be moved to index of 1)
        arrToBeSorted[i] = arrToBeSorted[minNum]
        # Fill the empty space with original num
        arrToBeSorted[minNum] = toBeSwitched
    return arrToBeSorted


print(selectionSort([3, 1, 2]))
