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

    def __str__(self):
        if not len(self.allTokenData):
            return "This object is empty"
        output_str = ""
        for token in self.allTokenData:
            output_str += str(token) + "\n"
        return output_str
###################################################################################
store = TokenCollection()

print("printing intial data")
store.update("t",[[0, 1]],[[0, 1]])
store.update("th",[[0, 2]],[[0, 2]])
store.update("thi",[[0, 3]],[[0, 3]])
store.update("this",[[0, 4]],[[0, 4]])
store.update("h",[[1, 2], [8, 9]],[[1, 2]])
store.update("hi",[[1, 3]],[[1, 3]])
store.update("his",[[1, 4]],[[1, 4]])
store.update("i",[[2, 3], [5, 6]],[[2, 3]])
store.update("is",[[2, 4], [5, 7]],[[2, 4]])
store.update("s",[[3, 4], [6, 7]],[[3, 4]])
store.update("i",[[2, 3], [5, 6]],[[2, 3]])
store.update("is",[[2, 4], [5, 7]],[[2, 4]])
store.update("s",[[3, 4], [6, 7]],[[3, 4]])
store.update("h",[[1, 2], [8, 9]],[[1, 2]])

print(store)
store.removeRedundantPairs()
print(store)

store.removeUnderlaps()
store.filter()
print(store)
store.cleanEmpty()
print(store)