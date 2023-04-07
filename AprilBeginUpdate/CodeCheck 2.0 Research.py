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

    # toString method
    #def __str__(self):
    #    if not len(self.allTokenData):
    #        return "This object is empty"
    #    output_str = ""
    #    for idx, token in enumerate(self.allTokenData):
    #        output_str += str(token)
    #        if idx != len(self.allTokenData) - 1:
    #            output_str += "\n"
    #    return output_str

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
        return self.tokenData
    
    # getter method for the inputADataStream
    def getADataStream(self):
        return self.tokenData.getADataStream()

    # getter method for the inputBDataStream
    def getBDataStream(self):
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

a = TokenAnalytics("this is a demo this is here dog cat this a is here","this blank is here for a demo",True)


#a = TokenAnalytics("this is a demo this is here dog cat this a is here alient have not landed",
#                   "this blank is here for a demo aliens have landed",True)

a = TokenAnalytics("The red kangaroo is the largest marsupial and can jump up to three times its own height."
    ,"According to recent studies, the red kangaroo, which is the largest marsupial, is capable of jumping up to three times its own height.",True)

x = a.getTokenData()
y = a.getADataStream()
z = a.getBDataStream()
print(x)
print(y)
print(z)

