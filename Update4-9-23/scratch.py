a = [
    [['this ', ' is here'], [0, 1], [0, 1]],
    [['this ', ' is here', 'this ', ' a demo'], [0, 3], [5, 8]],
    [[' is here', 'this ', ' a demo'], [1, 3], [6, 8]],
    [['this ', ' a demo'], [2, 3], [7, 8]],
    [['this ', ' is here'], [4, 5], [0, 1]],
    [['this ', ' is here'], [4, 5], [5, 6]]
]


##################################
class Pattern:
    def __init__(self, pattern):
        self.pattern = pattern
        self.inputAPairs = []
        self.inputBPairs = []

    def addData(self, inputAPair, inputBPair):
        self.inputAPairs.append(inputAPair)
        self.inputAPairs = list(set(map(tuple, self.inputAPairs)))
        self.inputAPairs = [list(x) for x in self.inputAPairs]
        self.inputBPairs.append(inputBPair)
        self.inputBPairs = list(set(map(tuple, self.inputBPairs)))
        self.inputBPairs = [list(x) for x in self.inputBPairs]

    def setInputAPairs(self,inputAPairs):
        self.inputAPairs = inputAPairs

    def setInputBPairs(self,inputBPairs):
        self.inputBPairs = inputBPairs

def managePatternObject(patternList, patternObjects):
    for patternObject in patternObjects:
        if patternObject.pattern == patternList:
            return patternObject
    newPatternObject = Pattern(patternList)
    patternObjects.append(newPatternObject)
    return newPatternObject

def getAPairs(patternObjects):
    result = []
    for patternObject in patternObjects:
        for i in range(len(patternObject.inputAPairs)):
            result.append(patternObject.inputAPairs[i])
    return result

def getBPairs(patternObjects):
    result = []
    for patternObject in patternObjects:
        for i in range(len(patternObject.inputBPairs)):
            result.append(patternObject.inputBPairs[i])
    return result

def removeAPairUnderlaps(patternObjects):
    for patternObject in patternObjects:
        i = 0
        while i < len(patternObject.inputAPairs):
            hasOverlap = False

            for comparison in getAPairs(patternObjects):
                if (patternObject.inputAPairs[i][0] >= comparison[0] and
                    patternObject.inputAPairs[i][1] <= comparison[1] and
                        (comparison != patternObject.inputAPairs[i])):
                    hasOverlap = True
                    break

            if hasOverlap:
                patternObject.inputAPairs.pop(i)
            else:
                i += 1

def removeBPairUnderlaps(patternObjects):
    for patternObject in patternObjects:
        i = 0
        while i < len(patternObject.inputBPairs):
            hasOverlap = False
            for comparison in getBPairs(patternObjects):
                if (patternObject.inputBPairs[i][0] >= comparison[0] and
                    patternObject.inputBPairs[i][1] <= comparison[1] and
                        (comparison != patternObject.inputBPairs[i])):
                    hasOverlap = True
                    break
            if hasOverlap:
                patternObject.inputBPairs.pop(i)
            else:
                i += 1

def removeEmptyPatterns(patternObjects):
    i = 0
    while i < len(patternObjects):
        if not patternObjects[i].inputAPairs or not patternObjects[i].inputBPairs:
            patternObjects.pop(i)
        else:
            i += 1

def removeIrrelevantPatterns(patternObjects):
    removeEmptyPatterns(patternObjects)

def processList(a):
    patternObjects = []
    for item in a:
        patternList = item[0]
        inputAPair = item[1]
        inputBPair = item[2]
        patternObject = managePatternObject(patternList, patternObjects)
        patternObject.addData(inputAPair, inputBPair)
    return patternObjects    
######################################################################################


result = processList(a)


print('---------------------')
for patternObject in result:
    print(f"Pattern: {patternObject.pattern}")
    print(f"Input A Pairs: {patternObject.inputAPairs}")
    print(f"Input B Pairs: {patternObject.inputBPairs}")
    print()
print("#########################")


removeAPairUnderlaps(result)
removeBPairUnderlaps(result)
removeEmptyPatterns(result)

print('---------------------')
for patternObject in result:
    print(f"Pattern: {patternObject.pattern}")
    print(f"Input A Pairs: {patternObject.inputAPairs}")
    print(f"Input B Pairs: {patternObject.inputBPairs}")
    print()
print("#########################")
