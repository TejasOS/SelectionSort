# TejasOpenSource

def selectionSort(arrToBeSorted):
    toBeSwitched = None
    minNum = 0
    for i in range(len(arrToBeSorted)): # For each element in array to be sorted, loop through array and see what minimum value is after that element
        for j in range(i+1, len(arrToBeSorted)):
            if (arrToBeSorted[j] < arrToBeSorted[minNum]):
                minNum = j

        toBeSwitched = arrToBeSorted[i] # Get current element at position that min needs to be switched to
        arrToBeSorted[i] = arrToBeSorted[minNum] # Move min num to correct pos (e.g. second smallest number would be moved to index of 1)
        arrToBeSorted[minNum] = toBeSwitched # Fill the empty space with original num
        minNum = i+1 # Set the minimum number pos to where we start looping again
    return arrToBeSorted


print(selectionSort([1, 3, 2]))

