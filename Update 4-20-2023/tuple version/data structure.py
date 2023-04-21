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
        # this was a tuple {} now it is a list
        self.allTokenData = {}

    def update(self, tokenString, inputATokenIndexes, inputBTokenIndexes):
        if tokenString in self.allTokenData:
            existing_obj = self.allTokenData[tokenString]
            existing_obj.inputATokenIndexes.extend(inputATokenIndexes)
            existing_obj.inputBTokenIndexes.extend(inputBTokenIndexes)
        else:
            self.allTokenData[tokenString] = Token(tokenString, inputATokenIndexes, inputBTokenIndexes)

    def removeRedundantPairs(self):
        for tokens in self.allTokenData.values():
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

    def removeUnderlapingPairs(self):
        for tokens in self.allTokenData.values():
            inputATokenIndexes = tokens.inputATokenIndexes
            inputBTokenIndexes = tokens.inputBTokenIndexes
            newInputATokenIndexes = []
            for pair in inputATokenIndexes:
                removePair = False
                for otherGivenTokens in self.allTokenData.values():
                    if otherGivenTokens is not tokens:
                        for otherPairs in otherGivenTokens.inputATokenIndexes:
                            if otherPairs[0] >= pair[0] and otherPairs[1] <= pair[1]:
                                removePair = True
                                break
                    if removePair:
                        break
                if not removePair:
                    newInputATokenIndexes.append(pair)
            tokens.inputATokenIndexes = newInputATokenIndexes

            newInputBTokenIndexes = []
            for pair in inputBTokenIndexes:
                removePair = False
                for otherGivenTokens in self.allTokenData.values():
                    if otherGivenTokens is not tokens:
                        for otherPairs in otherGivenTokens.inputBTokenIndexes:
                            if otherPairs[0] >= pair[0] and otherPairs[1] <= pair[1]:
                                removePair = True
                                break
                    if removePair:
                        break
                if not removePair:
                    newInputBTokenIndexes.append(pair)
            tokens.inputBTokenIndexes = newInputBTokenIndexes
        print("underlaps removed")



    def __str__(self):
        output = ''
        for tokenString, tokens in self.allTokenData.items():
            pairs_str = ', '.join([str(pair) for pair in tokens.inputATokenIndexes])
            pairs_str_2 = ', '.join([str(pair) for pair in tokens.inputBTokenIndexes])
            output += f'"{tokenString}" |\tA = [{pairs_str}]\n\tB = [{pairs_str_2}]\n'
        return output 

###########################################################################

allTokenData = TokenCollection()

allTokenData.update("T",[[0,1]],[[0,1]])
allTokenData.update("Th",[[0,2]],[[0,2]])
allTokenData.update("Thi",[[0,3]],[[0,3]])
allTokenData.update("This",[[0,4]],[[0,4]])
allTokenData.update("h",[[1,2],[8,9]],[[1,2]])
allTokenData.update("hi",[[1,3]],[[1,3]])
allTokenData.update("his",[[1,4]],[[1,4]])
allTokenData.update("i",[[2,3],[5,6]],[[2,3]])
allTokenData.update("is",[[2,4],[5,7]],[[2,4]])
allTokenData.update("s",[[3,4],[6,7]],[[3,4]])
allTokenData.update("i",[[2,3],[5,6]],[[2,3]])
allTokenData.update("is",[[2,4],[5,7]],[[2,3]])
allTokenData.update("s",[[3,4],[6,7]],[[3,4]])
allTokenData.update("h",[[1,2],[8,9]],[[1,2]])

print(allTokenData)
allTokenData.removeRedundantPairs()
print(allTokenData)
allTokenData.removeUnderlapingPairs()

print(allTokenData)
print("#################")
#allTokenData.clean()
print(allTokenData)