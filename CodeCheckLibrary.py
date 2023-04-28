"""
Written By:     Austin Daigle
Version:        1.0
Description:    This is a library that contains core algorithms
                for CodeCheck 2.0 and the ported legacy build of
                CodeCheck 1.0. This library offers CodeCheck 2.0
                which is a textual similarity analysis algorithm
                that identifies textual similarities between two
                inputs and returns a relative percentage score
                and the data on which tokens are identified to 
                be a positive match.
"""
#####################################################################
#  PROGRAM METHODS
#####################################################################
# getSimilarityHTML() METHOD
#********************************************************************
# the point of this method is to slide the input string 
# into section of matched and non-matched text in order
# to process it as formatted html code
def getSimilarityHTML(pattern, input):
    # extract the index pair sublist from each of the pattern list 
    # in the pattern superlist
    pattern = [sub[0] for sub in pattern]
    # Find the length of the input string
    maxValue= len(input)
    # Initialize an empty string to store the resulting string
    result = ""
    # Initialize a variable to keep track of the end of the previous slice
    lastRight = 0
    # Loop through each slice of the pattern in the input string
    for i in range(len(pattern)):
        # Get the left and right boundaries of the current slice
        left, right = pattern[i]
        # If the end of the previous slice does not match the beginning of the current slice
        if lastRight != left:
            # If the end of the previous slice is greater than the beginning of the current slice
            if lastRight > left:
                pass
            else:
                # update result the previous slice with a non-highlighted tag and append it to the result string
                result += input[lastRight:left]      
        # If there are more slices after the current one and the end of the current slice underlaps with the beginning of the next slice
        if i < len(pattern) - 1 and right > pattern[i + 1][0]:
            # Set the end of the current slice to the beginning of the next slice
            right = pattern[i + 1][0]
            # update the current slice with a highlighted tag and append it to the result string
            result += f"<mark>{input[left:right]}</mark>"
        else:
            # update the current slice with a highlighted tag and append it to the result string
            result += f"<mark>{input[left:right]}</mark>"
        # Set the end of the previous slice to the end of the current slice
        lastRight = right
    # If the end of the last slice does not match the end of the input string
    if lastRight != maxValue:
        # Print the last slice with a non-highlighted tag and append it to the result string
        result += input[lastRight:maxValue]
    # Return the resulting string
    return result

#********************************************************************
# calculatePercentage() METHOD
#********************************************************************
# this method is basically getSimilarityHTML() but simplified to
# return the percent of text that is identified as matched
# to the input string
def calculatePercentage(pattern, input):
    # extract the index pair sublist from each of the pattern list 
    # in the pattern superlist    
    pattern = [sub[0] for sub in pattern]
    # Get the maximum value to be used later
    maxValue = len(input)
    # Set up some variables to keep track of the input and matched sizes
    textInputSize = len(input)
    matchedInputSize = 0
    # Loop through each slice of the input string that matches the pattern
    for i in range(len(pattern)):
        # Get the left and right indices of the current slice
        left, right = pattern[i]
        # If the right index of the current slice is greater than the left index of the next slice,
        # set the right index to the left index of the next slice
        if i < len(pattern) - 1 and right > pattern[i + 1][0]:
            right = pattern[i + 1][0]
        # Add the length of the input string that falls within the current slice to the matched input size
        matchedInputSize += len(input[left:right])
    # Calculate the percentage of the input string that matched the pattern and format it to two decimal places
    percentMatched = "{:.2f}".format((matchedInputSize / textInputSize) * 100)
    # Return the percentage of the input string that matched the pattern
    return percentMatched

#********************************************************************
# findTokens() METHOD:
#********************************************************************
# this method returns all of the raw, unfiltered tokens shared 
# between two strings within the parameters
def findTokens(inputA, inputB,isCaseSensative):
    # case sensativity is enabled by default but can be 
    # modified if desired.
    # if case sensative, then set inputA/B to lowercase
    if isCaseSensative:
        inputA = inputA.lower()
        inputB = inputB.lower()
    # store the identified topens
    identifiedTokens = []
    # for 0 to the length of inputA
    for x in range(len(inputA)):
        # for x+1 to the lenght of inputA plus one
        for y in range(x+1,len(inputA)+1):
            # get substring between x and y in inputA
            subString = inputA[x:y]
            # if the substring is found in inputB then it is a 
            # raw token and then that token is added to identifiedTokens
            if subString in inputB:
                identifiedTokens.append(subString)
    # return the list of raw tokens
    return list(identifiedTokens)

#********************************************************************
# findAllTokenIndexes() METHOD:
#********************************************************************
# return all index pairs of the given token within a string to search.
def findAllTokenIndexes(string,token):
    # create a list to store the result
    result = []
    # by default case sensativity is respected by default
    isCaseSensative = False
    #result.append(token)
    startPosition = 0
    # while the start position is less than the lenth of the given string
    while startPosition < len(string):
        # if case sensative perform the find operation
        if(isCaseSensative):
            currentPosition = string.find(token, startPosition)
        # if not case sensative then perform the given find operation
        else:
            currentPosition = string.lower().find(token.lower(), startPosition)
        # if the start position is -1 then stop of the operation
        if currentPosition == -1:
            break
        # -1 added to correct offset error 
        # update the result
        result.append([currentPosition,currentPosition+len(token)])
        # update the startPosition variable
        startPosition = currentPosition + 1
    # return the final result
    return result

#####################################################################
# PROGRAM CLASSES
#####################################################################
# Token Class:
#********************************************************************
# This class stores token strings with their inputAIndexes and
# inputBIndexes
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

#********************************************************************
# TokenCollection class
#********************************************************************
# This class manages all of the token objects
class TokenCollection:
    # default constructor
    def __init__(self):
        # changed from a tuple to a list
        self.allTokenData = []
    # add token to Collection class object
    def update(self, tokenString, inputATokenIndexes, inputBTokenIndexes):
        # if the tokenString object already exists then update the existing
        # object witht he inputA and inputB TokenIndexess
        if tokenString in [token.tokenString for token in self.allTokenData]:
            existingObject = next(token for token in self.allTokenData if token.tokenString == tokenString)
            existingObject.inputATokenIndexes.extend(inputATokenIndexes)
            existingObject.inputBTokenIndexes.extend(inputBTokenIndexes)
        #if the object does not exist, then create it
        else:
            self.allTokenData.append(Token(tokenString, inputATokenIndexes, inputBTokenIndexes))
    # remove redundant index pairs from token objects in TokenCollection
    def removeRedundantPairs(self):
        for tokens in self.allTokenData:
            # create list to store result
            uniqueInputAPairs = []
            # for every pair in inputATokenIndexes for the given object
            # if the pair does not already exist then update the list
            for pair in tokens.inputATokenIndexes:
                if pair not in uniqueInputAPairs:
                    uniqueInputAPairs.append(pair)
            # update the inputATokenIndexes to the filtered result
            tokens.inputATokenIndexes = uniqueInputAPairs
            uniqueInputBPairs = []
            # for every pair in inputATokenIndexes for the given object
            # if the pair does not already exist then update the list
            for pair in tokens.inputBTokenIndexes:
                if pair not in uniqueInputBPairs:
                    uniqueInputBPairs.append(pair)
            # update the inputATokenIndexes to the filtered result
            tokens.inputBTokenIndexes = uniqueInputBPairs
        #print("redundant pairs removed")
    # remove underlapping index pairs from token objects in TokenCollection
    def removeUnderlaps(self):
        # underlap cleanup for inputATokenIndexes
        for token in range(0,len(self.allTokenData)):
            #print("*"+str(self.allTokenData[token]))
            pairsToRemove = []  # to store the index pairs to be removed from inputATokenIndexes
            for indexPair in self.allTokenData[token].inputATokenIndexes:
                #print("\t"+str(indexPair))
                for compareToken in range(0,len(self.allTokenData)):
                    # for every comparedIndexPair in allTokenData
                    for comparedIndexPair in self.allTokenData[compareToken].inputATokenIndexes:
                        if token == compareToken and indexPair == comparedIndexPair:
                            #print("\t\tomit")
                            pass
                        else:
                            if indexPair[0] >= comparedIndexPair[0] and indexPair[1] <= comparedIndexPair[1]:
                                #print("\t\t PAIR UNDERLAPPED UNDER: "+str(comparedIndexPair))
                                pairsToRemove.append(indexPair)  # add the underlapping pair to the removal list
                            else:
                                #print("\t\t"+str(comparedIndexPair))
                                pass
            self.allTokenData[token].inputATokenIndexes = [pair for pair in self.allTokenData[token].inputATokenIndexes if pair not in pairsToRemove]
        # same process as above but for inputBTokenIndexes
        for token in range(0,len(self.allTokenData)):
            #print("*"+str(self.allTokenData[token]))
            pairsToRemove = []  # to store the index pairs to be removed from inputATokenIndexes
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
                                pairsToRemove.append(indexPair)  # add the underlapping pair to the removal list
                            else:
                                #print("\t\t"+str(comparedIndexPair))
                                pass
            self.allTokenData[token].inputBTokenIndexes = [pair for pair in self.allTokenData[token].inputBTokenIndexes if pair not in pairsToRemove]
        #print("removing underlaping tokens")
    # remove empty token pairs from token objects in TokenCollection
    def cleanEmpty(self):
        #self.allTokenData = [token for token in self.allTokenData if token.inputATokenIndexes and token.inputBTokenIndexes]
        result = []
        for token in self.allTokenData:
            # if the indexes for inputA and inputB are both NOT empty then keep them 
            # and add them to the list to return
            if token.inputATokenIndexes and token.inputBTokenIndexes:
                result.append(token)
        # return the result
        self.allTokenData = result

    # remove single character tokens from the token Collection class
    def filter(self):
        # create list to store result
        filteredList = []
        # for every token in allTokenData
        for token in self.allTokenData:
            # if the length is over 1 then keep the entry
            if len(token.tokenString) > 1:
                filteredList.append(token)
        self.allTokenData = filteredList
        #print("filtering irrelevant tokens")
    # getter method to compile and return the datastream for inputA index stream
    def getADataStream(self):      
        stream = []
        # for every object in allTokenData
        for token in self.allTokenData:
            # update the inputAPairs from the current object values
            # for all of the pairs, append and create the data stream
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
            # update the inputBPairs from the current object values
            inputBPairs = token.getInputBTokenIndexes()
            # for all of the pairs, append and create the data stream
            for pairs in inputBPairs:
                stream.append([pairs,str(token.getTokenString())])
            #print("\t"+str(token.getTokenString()))
        stream = sorted(stream, key=lambda x: x[0])    
        return stream
    #def export(self):
    #    return self.allTokenData
    # toString method
    def __str__(self):
        # if the emptu is empty then return "this object is empty"
        if not len(self.allTokenData):
            return "This object is empty"
        result = ""
        # for every toke in the allTokenData add it to result
        for token in self.allTokenData:
            result += str(token) + "\n"
        # return result
        return result

#********************************************************************
# TokenAnalytics Class
# This class manages the token collection to clean up and process
# the data found from the token collection class
#********************************************************************
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

    # this method return the unique partially filtered tokens from inputA and inputB
    def getUniqueTokensStrings(self):
        # set allTokenStrings to every string from allTokenData
        allTokenStrings = [str(x.getTokenString()) for x in self.tokenData.allTokenData]
        # return the result
        return allTokenStrings

    # this method calculate the average lenght of tokens
    def getAverageTokenLength(self):
        # add all of the strings from the tokenData
        allTokenStrings = [str(x.getTokenString()) for x in self.tokenData.allTokenData]
        # take the leight of the allTokenStrings and divide that by the lenghth of allTokenStrings
        averageTokenLength = sum(len(token) for token in allTokenStrings)/len(allTokenStrings)
        # return the average
        return averageTokenLength

    # this method delete all information in this object
    def clear(self):
        self.inputA = None
        self.inputB = None
        self.isCaseSensative = None
        self.tokenData = TokenCollection()

#####################################################################
# CODECHECK ENGINES
#####################################################################
# These are methods that actually perform analytical process
# of textual analysis
#####################################################################

# this method returns just the shared tokens between inputA and inputB
# this method does not remove token fragments that are cross-shared
# between actually tokens.
def getRawTokens(inputA,inputB,isCaseSensative):
    return findTokens(inputA, inputB,isCaseSensative)

# this method returns the shared tokens between inputA and inputB
# however it does remove the token fragments that are redundant.
# Some irrelevant tokens may be present since CodeCheck 2.0's
# pattern recognition algorithm was not implemented in this method.
def getRefinedTokens(inputA,inputB):
    allTokenData = TokenAnalytics(inputA,inputB,True)
    # return the all of the uniqueTokenStrings 
    return allTokenData.getUniqueTokensStrings()

# This is the optimized legacy algorithm for CodeCheck 1.0
# This algorithm does not analyze the usage of tokens
# between inputs but instead it just checks raw matches 
# of tokens between two inputs and not how they are use.
def codeCheckLegacy(inputA,inputB):
    allTokenData = TokenAnalytics(inputA,inputB,True)
    #x = a.getTokenData()
    rawAStream = allTokenData.getADataStream()
    rawBStream = allTokenData.getBDataStream()

    # get similarity formatted html for both of the inputs relative to eachother
    inputAFormattedHTML = getSimilarityHTML(rawAStream,inputA)
    inputBFormattedHTML = getSimilarityHTML(rawBStream,inputB)

    # get similarity percentage score for both of the input relative to eachother
    inputASimilarityPercentage = calculatePercentage(rawAStream,inputA)
    inputBSimilarityPercentage = calculatePercentage(rawBStream,inputB)
    # put all of the variables/objects to return into a single list for
    # easse of consolidation.
    result = [rawAStream,
        inputASimilarityPercentage,
        inputAFormattedHTML,rawBStream,
        inputBSimilarityPercentage,
        inputBFormattedHTML]
    # return the result
    return result


def codeCheck2(inputA,inputB):
    # get all token data from inputs
    allTokenData = TokenAnalytics(inputA,inputB,True)
    # save the raw data stream data
    rawAStream = allTokenData.getADataStream()
    rawBStream = allTokenData.getBDataStream()

    ################################################
    # PATTERN CLASS
    # Internal Class
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
        # default constructor
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
        # for every patternObject in patternObjects        
        for patternObject in patternObjects:
            # if the patrtern is equal to patternlist then return patternObject
            if patternObject.pattern == patternList:
                return patternObject
        # otherwise make a new pattern object and return that
        newPatternObject = Pattern(patternList)
        patternObjects.append(newPatternObject)
        return newPatternObject
    # this returns all of the inputAPairs from all of the object in the class
    def getAPairs(patternObjects):
        result = []
        # for every patternObject in patternObjects
        for patternObject in patternObjects:
            for i in range(len(patternObject.inputAPairs)):
                # update the result with inputAPairs from patternObject
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
            # while the value of i is less than the patternObject inputAPairs
            while i < len(patternObject.inputAPairs):
                hasUnderLap = False
                for comparison in getAPairs(patternObjects):
                    # if the current pair is inside of other pair then discard as an underlap
                    if (patternObject.inputAPairs[i][0] >= comparison[0] and
                        patternObject.inputAPairs[i][1] <= comparison[1] and
                        (comparison != patternObject.inputAPairs[i])):
                        hasUnderLap = True
                        break
                # if an underlap is present then discard
                if hasUnderLap:
                    patternObject.inputAPairs.pop(i)
                # updat the value of i
                else:
                    i += 1
    # remove the underlapping pairs for inputBPairs
    def removeBPairUnderlaps(patternObjects):
        # for every patternObject in patternObject
        for patternObject in patternObjects:
            i = 0
            # while i is less than the lenght of patternObject inputBPairs
            while i < len(patternObject.inputBPairs):
                hasUnderLap = False
                for comparison in getBPairs(patternObjects):
                    # a -1 was added after patternObject.inputBPairs[i][1] to fix pattern offset errors
                    # if the current pair is inside of other pair then discard as an underlap
                    if (patternObject.inputBPairs[i][0] >= comparison[0] and
                        patternObject.inputBPairs[i][1] <= comparison[1] and
                            (comparison != patternObject.inputBPairs[i])):
                        hasUnderLap = True
                        break          
                # if there is an underlap then discard
                if hasUnderLap:
                    patternObject.inputBPairs.pop(i)
                # update the value of i
                else:
                    i += 1
    # for every sublist (object update)
    # inside of the the parsed input
    # process that and update the process
    # class object
    def processList(input):
        # create a list to store the pattern objects
        patternObjects = []
        # for every item in the list
        for item in input:
            patternList = item[0]
            inputAPair = item[1]
            inputBPair = item[2]
            patternObject = managePatternObject(patternList, patternObjects)
            patternObject.addData(inputAPair, inputBPair)
        # return the patternObject object
        return patternObjects
    # remove an empty pattern object
    # from the pattern class if 
    # either the inputAPairs or inputBPairs
    # are empty
    def removeEmptyPatterns(patternObjects):
        i = 0
        # while is less than the length of the patternObjects
        while i < len(patternObjects):
            # if there is a pattern that is empty then remove it
            if not patternObjects[i].inputAPairs or not patternObjects[i].inputBPairs:
                patternObjects.pop(i)
            # update the index counter
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
                    # using the value of i and k with length of a and b with intersections
                    # cross compare and identify shared patterns
                    while i + k < len(a) and j + k < len(b) and a[i + k] == b[j + k]:
                        sharedPattern.append(a[i + k])
                        aIndices[1] = i + k
                        bIndices[1] = j + k
                        k += 1
                    # FIX: the second condition was added to solve the issue of dropping
                    #   clusters with multiple words in it
                    # IF the pattern is longer than 1 element 
                    # OR the element has two or more words in it, 
                    # THEN add it to the result
                    if len(sharedPattern) > 1 or bool(len(sharedPattern[0].split()) > 2):
                        result.append([sharedPattern, aIndices, bIndices])
        # return the given list entry
        return result
    ##########################################################
    unProcessedPatterns = findSharedPatterns([x[1] for x in rawAStream],[x[1] for x in rawBStream])
    processedPatterns = processList(unProcessedPatterns)
    # clean the data
    removeAPairUnderlaps(processedPatterns)
    removeBPairUnderlaps(processedPatterns)
    removeEmptyPatterns(processedPatterns)
    # create the variables that store the final processed pattern data
    filteredAStream = []
    filteredBStream = []
    # for every pattern object inside of the processedPatterns object
    for patternObject in processedPatterns:
        #print(f"Pattern: {patternObject.pattern}")
        #print(f"\tInput A Pairs: {patternObject.inputAPairs}")
        # for every index pair inside of inputAPairs for the given pattern
        for pairs in patternObject.inputAPairs:
            filteredAStream += rawAStream[pairs[0]:pairs[1]+1]
        #print(f"\tInput B Pairs: {patternObject.inputBPairs}")
        # for every index pair inside of inputBPairs for the given pattern
        for pairs in patternObject.inputBPairs:
            filteredBStream += rawBStream[pairs[0]:pairs[1]+1]
    # get similarity formatted html for both of the inputs relative to eachother
    inputAFormattedHTML = getSimilarityHTML(filteredAStream,inputA)
    inputBFormattedHTML = getSimilarityHTML(filteredBStream,inputB)
    # get similarity percentage score for both of the input relative to eachother
    inputASimilarityPercentage = calculatePercentage(filteredAStream,inputA)
    inputBSimilarityPercentage = calculatePercentage(filteredBStream,inputB)
    # compile the results into a single list to return
    result = [filteredAStream,
        inputASimilarityPercentage,
        inputAFormattedHTML,
        filteredBStream,
        inputBSimilarityPercentage,
        inputBFormattedHTML]
    # return the result
    return result
    
#********************************************************************
# Actual Code
#********************************************************************

print(codeCheck2("The quick brown fox jumps over the lazy dog.",
            "The fast brown fox leaps over the idle canine."))
