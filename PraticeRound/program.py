import sys

inputName = sys.argv[1]
outputName = inputName.split('/')[-1].split('.')[0]+".out"
fileInput = open(inputName, "r")

[MAX_SLICES, PIZZA_TYPE] = [int(x)
                            for x in fileInput.readline().strip().split(' ')]

pizzas = [int(x) for x in fileInput.readline().strip().split(' ')]
selected = [False for x in range(PIZZA_TYPE+1)]


def max(a, b):
    if a > b:
        return a
    return b


def createTraceTable(A):
    for j in range(1, PIZZA_TYPE + 1):
        for i in range(1, MAX_SLICES+1):
            if pizzas[j] > i:
                A[j][i] = A[j-1][i]
            else:
                A[j][i] = max(A[j-1][i], pizzas[j]+A[j-1][i-pizzas[j]])


def getMaxSlices(traceTable, maxValue):
    result = []
    for j in range(PIZZA_TYPE+1):
        result.append(traceTable[j][maxValue])
    return result


def selectPizza(traceTable, maxValue):
    maxSlices = getMaxSlices(traceTable, maxValue)
    for j in range(PIZZA_TYPE, 0, -1):
        if pizzas[j] <= maxSlices[j] and selected[j] == False:
            selected[j] = True
            return maxValue - pizzas[j]
    return 0


def tracing(traceTable):
    remaining = MAX_SLICES
    count = -1
    while remaining > 0:
        remaining = selectPizza(traceTable, remaining)
        count += 1
    return count


def approximate(max_slices, pizza_type, pizzas):
    result = 0
    count = 0
    for i in range(pizza_type-1, -1, -1):
        result += pizzas[i]
        count += 1
        selected[i+1] = True
        if result > max_slices:
            result -= pizzas[i]
            selected[i+1] = False
            count -= 1
            return count
    return count


def createOutputFile(count):
    fileOutput = open(outputName, "w")
    fileOutput.write(str(count)+"\n")
    result = ""
    for i in range(len(selected)):
        if selected[i]:
            result += str(i-1)+" "
    result = result.strip()
    fileOutput.write(result)
    fileOutput.close()


def approximateMethod():
    count = approximate(MAX_SLICES, PIZZA_TYPE, pizzas)
    createOutputFile(count)


def dynamicMethod():
    A = [[0 for x in range(MAX_SLICES+1)] for x in range(PIZZA_TYPE+1)]
    createTraceTable(A)
    count = tracing(A)
    createOutputFile(count)


if MAX_SLICES > 100000 or PIZZA_TYPE > 1000:
    approximateMethod()
else:
    pizzas.insert(0, 0)
    dynamicMethod()
