
#--------------------------------------
class Token:
    def __init__(self, tokenString, inputATokenIndexes, inputBTokenIndexes):
        self.inputATokenIndexes = inputATokenIndexes
        self.inputBTokenIndexes = inputBTokenIndexes
        self.tokenString = tokenString

    def getTokenString(self):
        return self.tokenString
    
    def getInputATokenIndexes(self):
        return self.inputATokenIndexes
    
    def getInputBTokenIndexes(self):
        return self.inputBTokenIndexes

    def __str__(self):
        return "\""+self.tokenString+"\" | A = "+str(self.inputATokenIndexes)+" | B = "+str(self.inputBTokenIndexes)

class TokenCollection:
    def __init__(self):
        # changed from a tuple to a list
        self.allTokenData = []

    def update(self, tokenString, inputATokenIndexes, inputBTokenIndexes):
        if tokenString in [token.tokenString for token in self.allTokenData]:
            existing_obj = next(token for token in self.allTokenData if token.tokenString == tokenString)
            existing_obj.inputATokenIndexes.extend(inputATokenIndexes)
            existing_obj.inputBTokenIndexes.extend(inputBTokenIndexes)
        else:
            self.allTokenData.append(Token(tokenString, inputATokenIndexes, inputBTokenIndexes))

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
        print("redundant pairs removed")

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
        print("removing underlaping tokens")

    def cleanEmpty(self):
        #self.allTokenData = [token for token in self.allTokenData if token.inputATokenIndexes and token.inputBTokenIndexes]
        result = []
        for token in self.allTokenData:
            if token.inputATokenIndexes and token.inputBTokenIndexes:
                result.append(token)
        self.allTokenData = result

        print("empty tokens removed")

    def filter(self):
        
        filteredList = []
        
        for token in self.allTokenData:
            if len(token.tokenString) > 1:
                filteredList.append(token)
        self.allTokenData = filteredList
        print("filtering irrelevant tokens")

    def getADataStream(self):      
        stream = []
        for token in self.allTokenData:
            inputAPairs = token.getInputATokenIndexes()
            for pairs in inputAPairs:
                stream.append([pairs,str(token.getTokenString())])
            #print("\t"+str(token.getTokenString()))
        
        stream = sorted(stream, key=lambda x: x[0])
        return stream


    def getBDataStream(self):      
        stream = []
        for token in self.allTokenData:
            inputBPairs = token.getInputBTokenIndexes()
            for pairs in inputBPairs:
                stream.append([pairs,str(token.getTokenString())])
            #print("\t"+str(token.getTokenString()))

        stream = sorted(stream, key=lambda x: x[0])    
        return stream


    def __str__(self):
        if not len(self.allTokenData):
            return "This object is empty"
        output_str = ""
        for token in self.allTokenData:
            output_str += str(token) + "\n"
        return output_str
#--------------------------------------

#######################################
# this method returns all of the 
# raw, unfiltered tokens shared between
# two strings within the parameters
#######################################
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



#######################################
# return all index pairs of the 
# given token within a string 
# to search.
#######################################
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

def compileTokenData(inputA,inputB,isCaseSensative):
    store = TokenCollection()
    
    tokens = findTokens(inputA, inputB,isCaseSensative)
    print("=========================================================")
    print("InputA: \""+str(inputA)+"\"")
    print("InputB: \""+str(inputB)+"\"")
    print("")
    print("*** All Identified Tokens shared between inputA and inputB ***")
    print("=========================================================")
    print(tokens)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #filter tokens list here using filter parameters
    print("Token\tinputA\tInputB")
    for items in tokens:
        store.update(str(items),findAllTokenIndexes(inputA,items),findAllTokenIndexes(inputB,items))

    #print(store)
    store.removeRedundantPairs()
    #print(store)
    store.removeUnderlaps()
    store.filter()
    store.cleanEmpty()

    print("--- token collection data ---")

    print(store)
    print("--- getADataStream: ---")
    a = store.getADataStream()
    for x in a:
        print(x)
    print("--- getBDataStream: ---")
    b = store.getBDataStream()
    for x in b:
        print(x)


############################################


compileTokenData("this is a demo this is here"
                ,"this blank is here for a demo",True)

