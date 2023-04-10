#***********************************************
# PROGRAM INPUT
#***********************************************
a = ['this ', ' is here','this ', ' a demo', 'this ', ' is here', ' cat', ' this ', ' is here']
b = ['this ', ' is here', ' dork', 'this ', 'cookie ', 'this ', ' is here','this ', ' a demo']

################################################
# PATTERN CLASS
################################################
# this is a the class that take in and processes the
# list and generated by the findSharedPatterns()
# method, each of the repetitions of the list 
# have a unique pattern saved to the class and 
# for every reidentifid pattern the data
# for the given object is updated, then the
# data is cleaned and reformed with only
# relevant information.

class Pattern:
    def __init__(self, pattern):
        self.pattern = pattern
        self.inputAPairs = []
        self.inputBPairs = []

    # add inputAPair and inputBPair data into existing data lists
    def addData(self, inputAPair, inputBPair):
        self.inputAPairs.append(inputAPair)
        self.inputAPairs = list(set(map(tuple, self.inputAPairs)))
        self.inputAPairs = [list(x) for x in self.inputAPairs]
        self.inputBPairs.append(inputBPair)
        self.inputBPairs = list(set(map(tuple, self.inputBPairs)))
        self.inputBPairs = [list(x) for x in self.inputBPairs]

#*********************************************
# This methods are for managing the pattern class
# this find or creates objects as needed be
def managePatternObject(patternList, patternObjects):
    for patternObject in patternObjects:
        if patternObject.pattern == patternList:
            return patternObject
    newPatternObject = Pattern(patternList)
    patternObjects.append(newPatternObject)
    return newPatternObject

# this returns all of the inputAPairs from all of the object in the class
def getAPairs(patternObjects):
    result = []
    for patternObject in patternObjects:
        for i in range(len(patternObject.inputAPairs)):
            result.append(patternObject.inputAPairs[i])
    return result

# this returns all of the inputBPairs from all of the object in the class
def getBPairs(patternObjects):
    result = []
    for patternObject in patternObjects:
        for i in range(len(patternObject.inputBPairs)):
            result.append(patternObject.inputBPairs[i])
    return result

# remove the underlapping pairs for inputAPairs
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

# remove the underlapping pairs for inputBPairs
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

# for every sublist (object update)
# inside of the the parsed input
# process that and update the process
# class object
def processList(input):
    patternObjects = []
    for item in input:
        patternList = item[0]
        inputAPair = item[1]
        inputBPair = item[2]
        patternObject = managePatternObject(patternList, patternObjects)
        patternObject.addData(inputAPair, inputBPair)
    return patternObjects

# remove an empty pattern object
# from the pattern class if 
# either the inputAPairs or inputBPairs
# are empty
def removeEmptyPatterns(patternObjects):
    i = 0
    while i < len(patternObjects):
        if not patternObjects[i].inputAPairs or not patternObjects[i].inputBPairs:
            patternObjects.pop(i)
        else:
            i += 1

# this method is used to drive the empty 
# object removal method above.
def removeIrrelevantPatterns(patternObjects):
    removeEmptyPatterns(patternObjects)

#***********************************************
# CROSS REFERENCING PATTERN ALGORITHM:
#***********************************************

# this method take in two list of strings and goes through
# and identified all patterns of string of two 
# or more strings in a sequential order.
# these patterns are returned as a series of list in
# the format below: [pattern][inputAPair][inputBPair]
# each of the patterns are identified and merged together
# in a set of list inside of list, so patterns 
# will be repeated but with different data points 

""" This is an example output of the findSharedPatterns() method   
    [['this ', ' is here'], [0, 1], [0, 1]],
    [['this ', ' is here', 'this ', ' a demo'], [0, 3], [5, 8]],
    [[' is here', 'this ', ' a demo'], [1, 3], [6, 8]],"""

def findSharedPatterns(a, b):
    result = []
    for i in range(len(a)):
        for j in range(len(b)):
            # Check if the current elements match
            if a[i] == b[j]:
                # Initialize the shared pattern and indices
                sharedPattern = [a[i]]
                aIndices = [i, i]
                bIndices = [j, j]
                # Check for matching subsequent elements
                k = 1
                while i + k < len(a) and j + k < len(b) and a[i + k] == b[j + k]:
                    sharedPattern.append(a[i + k])
                    aIndices[1] = i + k
                    bIndices[1] = j + k
                    k += 1
                # If the pattern is longer than 1 element, add it to the result
                if len(sharedPattern) > 1:
                    result.append([sharedPattern, aIndices, bIndices])
    # return the given list entry
    return result

##########################################################

unProcessedPatterns = findSharedPatterns(a,b)

processedPatterns = processList(unProcessedPatterns)
removeAPairUnderlaps(processedPatterns)
removeBPairUnderlaps(processedPatterns)
removeEmptyPatterns(processedPatterns)

print('---------------------')
for patternObject in processedPatterns:
    print(f"Pattern: {patternObject.pattern}")
    print(f"Input A Pairs: {patternObject.inputAPairs}")
    print(f"Input B Pairs: {patternObject.inputBPairs}")
    print()
print("#########################")