#********************************
# FINDTOKEN METHOD
# this method returns all of the 
# raw, unfiltered tokens shared 
# between two strings within the 
# parameters
#********************************

def findTokens(inputA, inputB,isCaseSensative):
    if isCaseSensative:
        inputA = inputA.lower()
        inputB = inputB.lower()
    identifiedTokens = []
    for x in range(len(inputA)):
        for y in range(x+1,len(inputA)+1):
            subString = inputA[x:y]
            if subString in inputB:
                identifiedTokens.append(subString)

    return list(identifiedTokens)

#*********************************
# FINDALLTOKENSINDEXES METHOD
# return all index pairs of the 
# given token within a string 
# to search.
#*********************************
def findAllTokenIndexes(string,token):
    # by default case sensativity is respected by default
    result = []
    isCaseSensative = False
    #result.append(token)
    startPosition = 0
    while startPosition < len(string):
        if(isCaseSensative):
            currentPosition = string.find(token, startPosition)
        else:
            currentPosition = string.lower().find(token.lower(), startPosition)
        if currentPosition == -1:
            break
        # -1 added to correct offset error 
        result.append([currentPosition,currentPosition+len(token)])
        startPosition = currentPosition + 1
    return result

#-------------------------------- 
#Token Class
#--------------------------------
class Token:
    #default constructor
    def __init__(self, tokenString, inputATokenIndexes, inputBTokenIndexes):
        self.inputATokenIndexes = inputATokenIndexes
        self.inputBTokenIndexes = inputBTokenIndexes
        self.tokenString = tokenString

    # getter method for tokenString
    def getTokenString(self):
        return self.tokenString
    
    # getter method for inputATokenIndexes
    def getInputATokenIndexes(self):
        return self.inputATokenIndexes

    # getter method for inputBTokenIndexes    
    def getInputBTokenIndexes(self):
        return self.inputBTokenIndexes

    # toString method for token class
    def __str__(self):
        return "\""+self.tokenString+"\" | A = "+str(self.inputATokenIndexes)+" | B = "+str(self.inputBTokenIndexes)

#--------------------------------
# TokenCollection class
#--------------------------------
class TokenCollection:
    # default constructor
    def __init__(self):
        # changed from a tuple to a list
        self.allTokenData = []

    # add token to Collection class object
    def update(self, tokenString, inputATokenIndexes, inputBTokenIndexes):
        if tokenString in [token.tokenString for token in self.allTokenData]:
            existing_obj = next(token for token in self.allTokenData if token.tokenString == tokenString)
            existing_obj.inputATokenIndexes.extend(inputATokenIndexes)
            existing_obj.inputBTokenIndexes.extend(inputBTokenIndexes)
        else:
            self.allTokenData.append(Token(tokenString, inputATokenIndexes, inputBTokenIndexes))

    # remove redundant index pairs from token objects in TokenCollection
    def removeRedundantPairs(self):
        for tokens in self.allTokenData:
            uniqueInputAPairs = []
            for pair in tokens.inputATokenIndexes:
                if pair not in uniqueInputAPairs:
                    uniqueInputAPairs.append(pair)
            tokens.inputATokenIndexes = uniqueInputAPairs
            uniqueInputBPairs = []
            for pair in tokens.inputBTokenIndexes:
                if pair not in uniqueInputBPairs:
                    uniqueInputBPairs.append(pair)
            tokens.inputBTokenIndexes = uniqueInputBPairs
        #print("redundant pairs removed")

    # remove underlapping index pairs from token objects in TokenCollection
    def removeUnderlaps(self):
        # underlap cleanup for inputATokenIndexes
        for token in range(0,len(self.allTokenData)):
            #print("*"+str(self.allTokenData[token]))
            pairs_to_remove = []  # to store the index pairs to be removed from inputATokenIndexes
            for indexPair in self.allTokenData[token].inputATokenIndexes:
                #print("\t"+str(indexPair))
                for compareToken in range(0,len(self.allTokenData)):
                    for comparedIndexPair in self.allTokenData[compareToken].inputATokenIndexes:
                        if token == compareToken and indexPair == comparedIndexPair:
                            #print("\t\tomit")
                            pass
                        else:
                            if indexPair[0] >= comparedIndexPair[0] and indexPair[1] <= comparedIndexPair[1]:
                                #print("\t\t PAIR UNDERLAPPED UNDER: "+str(comparedIndexPair))
                                pairs_to_remove.append(indexPair)  # add the overlapping pair to the removal list
                            else:
                                #print("\t\t"+str(comparedIndexPair))
                                pass
            self.allTokenData[token].inputATokenIndexes = [pair for pair in self.allTokenData[token].inputATokenIndexes if pair not in pairs_to_remove]
        # underlap cleanup for inputATokenIndexes
        for token in range(0,len(self.allTokenData)):
            #print("*"+str(self.allTokenData[token]))
            pairs_to_remove = []  # to store the index pairs to be removed from inputATokenIndexes
            for indexPair in self.allTokenData[token].inputBTokenIndexes:
                #print("\t"+str(indexPair))
                for compareToken in range(0,len(self.allTokenData)):
                    for comparedIndexPair in self.allTokenData[compareToken].inputBTokenIndexes:
                        if token == compareToken and indexPair == comparedIndexPair:
                            #print("\t\tomit")
                            pass
                        else:
                            if indexPair[0] >= comparedIndexPair[0] and indexPair[1] <= comparedIndexPair[1]:
                                #print("\t\t PAIR UNDERLAPPED UNDER: "+str(comparedIndexPair))
                                pairs_to_remove.append(indexPair)  # add the overlapping pair to the removal list
                            else:
                                #print("\t\t"+str(comparedIndexPair))
                                pass
            self.allTokenData[token].inputBTokenIndexes = [pair for pair in self.allTokenData[token].inputBTokenIndexes if pair not in pairs_to_remove]
        #print("removing underlaping tokens")

    # remove empty token pairs from token objects in TokenCollection
    def cleanEmpty(self):
        #self.allTokenData = [token for token in self.allTokenData if token.inputATokenIndexes and token.inputBTokenIndexes]
        result = []
        for token in self.allTokenData:
            if token.inputATokenIndexes and token.inputBTokenIndexes:
                result.append(token)
        self.allTokenData = result
        #print("empty tokens removed")

    # remove single character tokens from the token Collection class
    def filter(self):
        filteredList = []
        for token in self.allTokenData:
            if len(token.tokenString) > 1:
                filteredList.append(token)
        self.allTokenData = filteredList
        #print("filtering irrelevant tokens")

    # getter method to compile and return the datastream for inputA index stream
    def getADataStream(self):      
        stream = []
        for token in self.allTokenData:
            inputAPairs = token.getInputATokenIndexes()
            for pairs in inputAPairs:
                stream.append([pairs,str(token.getTokenString())])
            #print("\t"+str(token.getTokenString()))
        stream = sorted(stream, key=lambda x: x[0])
        return stream

    # getter method to compile and return the datastream for inputB index stream
    def getBDataStream(self):      
        stream = []
        for token in self.allTokenData:
            inputBPairs = token.getInputBTokenIndexes()
            for pairs in inputBPairs:
                stream.append([pairs,str(token.getTokenString())])
            #print("\t"+str(token.getTokenString()))
        stream = sorted(stream, key=lambda x: x[0])    
        return stream

    #def export(self):
    #    return self.allTokenData

    # toString method
    def __str__(self):
        if not len(self.allTokenData):
            return "This object is empty"
        output_str = ""
        for token in self.allTokenData:
            output_str += str(token) + "\n"
        return output_str

#--------------------------------
# TokenAnalytics Class
#--------------------------------
class TokenAnalytics:

    # default constructor
    def __init__(self,inputA,inputB,isCaseSensative):
        self.inputA = inputA
        self.inputB = inputB
        self.isCaseSensative = isCaseSensative
        # create tokenCollection object
        self.tokenData = TokenCollection()
        self.update(inputA,inputB,isCaseSensative)

    # update the token data for tokenData
    def update(self,inputA,inputB,isCaseSensative):
        tokens = findTokens(inputA, inputB,isCaseSensative)
        # for every token in tokens update tokenData object
        for items in tokens:
            self.tokenData.update(str(items),findAllTokenIndexes(inputA,items),findAllTokenIndexes(inputB,items))
        # perform data cleaning functions for tokenData
        self.tokenData.removeRedundantPairs()
        self.tokenData.removeUnderlaps()
        self.tokenData.filter()
        self.tokenData.cleanEmpty()

    # getter method for inputA
    def getInputA(self):
        return self.getInputA
    
    # setter method for inputA
    def setInputA(self, inputA):
        self.inputA = inputA
        self.update(self.inputA,self.inputB,self.isCaseSensative)

    # getter method for inputB
    def getInputB(self):
        return self.getInputB
    
    # setter method for inputB
    def setInputB(self, inputB):
        self.inputB = inputB
        self.update(self.inputA,self.inputB,self.isCaseSensative)

    # getter method for isCaseSensative
    def getIsCaseSensative(self):
        return self.isCaseSensative
    
    # setter method for isCaseSensative
    def setIsCaseSensative(self,isCaseSensative):
        self.isCaseSensative = isCaseSensative
        self.update(self.inputA,self.inputB,self.isCaseSensative)

    # getter method for the tokenData
    def getTokenData(self):
        # this returns a "database" of all of the token
        # data shared between inputA and inputB
        return self.tokenData
    
    # getter method for the inputADataStream
    def getADataStream(self):
        # this is the data that is used for raw similarity analytics
        return self.tokenData.getADataStream()

    # getter method for the inputBDataStream
    def getBDataStream(self):
        # this is the data that is used for raw similarity analytics
        return self.tokenData.getBDataStream()

    def getAverageTokenLength(self):
        allTokenStrings = [str(x.getTokenString()) for x in self.tokenData.allTokenData]
        averageTokenLength = sum(len(token) for token in allTokenStrings)/len(allTokenStrings)
        return averageTokenLength

    # this method delete all information in this object
    def clear(self):
        self.inputA = None
        self.inputB = None
        self.isCaseSensative = None
        self.tokenData = TokenCollection()

#=====================================================

######################################################
#   CODECHECK ENGINES
######################################################


# this is the optimized legacy algorithm for CodeCheck 1.0
def codeCheckLegacy(inputA,inputB):
    allTokenData = TokenAnalytics(inputA,inputB,True)
    #x = a.getTokenData()
    rawAStream = allTokenData.getADataStream()
    rawBStream = allTokenData.getBDataStream()
    print("CodeCheck 1.0 Legacy Analysis Algorithm")
    #print(rawAStream)
    #print(rawBStream)
    #codeCheckLegacy("this is a demo this is here dog cat this a is here","this blank is here for a demo")


def codeCheck2(inputA,inputB):
    #[x[1] for x in a]
    allTokenData = TokenAnalytics(inputA,inputB,True)
    #x = a.getTokenData()
    rawAStream = allTokenData.getADataStream()
    rawBStream = allTokenData.getBDataStream()
    print("CodeCheck 2.0 Analysis Algorithm")
    #print(rawAStream)
    #print(rawBStream)


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
    
    unProcessedPatterns = findSharedPatterns([x[1] for x in rawAStream],[x[1] for x in rawBStream])

    processedPatterns = processList(unProcessedPatterns)
    removeAPairUnderlaps(processedPatterns)
    removeBPairUnderlaps(processedPatterns)
    removeEmptyPatterns(processedPatterns)

    for patternObject in processedPatterns:
        print(f"Pattern: {patternObject.pattern}")
        print(f"Input A Pairs: {patternObject.inputAPairs}")
        print(f"Input B Pairs: {patternObject.inputBPairs}")
        print()
    

    
#######################################################
codeCheck2("this is a demo this is here dog cat this a is here","this blank is here for a demo")