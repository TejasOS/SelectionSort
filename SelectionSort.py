# TejasOpenSource

def selectionSort(arrToBeSorted):
    toBeSwitched = None
    minNum = 0
    minCounter = 0
    for i in range(len(arrToBeSorted)):
        for j in range(minCounter, len(arrToBeSorted)):
            if (arrToBeSorted[j] < arrToBeSorted[minNum]):
                minNum = j

        toBeSwitched = arrToBeSorted[i]
        arrToBeSorted[i] = arrToBeSorted[minNum]
        arrToBeSorted[minNum] = toBeSwitched
        minCounter += 1
        minNum = minCounter
    return arrToBeSorted


print(selectionSort([1, 3, 2]))
