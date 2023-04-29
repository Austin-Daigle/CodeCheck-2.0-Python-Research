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
        if not len(self.allTokenData):
            return "This object is empty"        
        stream = []
        for token in self.allTokenData:
            inputAPairs = token.getInputATokenIndexes()
            for pairs in inputAPairs:
                stream.append([pairs,str(token.getTokenString())])
            #print("\t"+str(token.getTokenString()))
        
        #stream =sorted(stream, key=lambda x: x[0])
        for x in stream:
            print(x)
        return stream


    def getBDataStream(self):
        if not len(self.allTokenData):
            return "This object is empty"        
        stream = []
        for token in self.allTokenData:
            inputBPairs = token.getInputBTokenIndexes()
            for pairs in inputBPairs:
                stream.append([pairs,str(token.getTokenString())])
            #print("\t"+str(token.getTokenString()))

        #stream =sorted(stream, key=lambda x: x[0])    
        for x in stream:
            print(x)
        return stream


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
store.update("t",[[0, 1], [26, 27], [35, 36]],[[24, 25], [31, 32]])
store.update("th",[[0, 2]],[[31, 33]])
store.update("thi",[[0, 3]],[[31, 34]])
store.update("this",[[0, 4]],[[31, 35]])
store.update("this ",[[0, 5]],[[31, 36]])
store.update("this i",[[0, 6]],[[31, 37]])
store.update("this is",[[0, 7]],[[31, 38]])
store.update("this is ",[[0, 8]],[[31, 39]])
store.update("this is e",[[0, 9]],[[31, 40]])
store.update("this is ex",[[0, 10]],[[31, 41]])
store.update("this is exa",[[0, 11]],[[31, 42]])
store.update("this is exam",[[0, 12]],[[31, 43]])
store.update("this is examp",[[0, 13]],[[31, 44]])
store.update("this is exampl",[[0, 14]],[[31, 45]])
store.update("this is example",[[0, 15]],[[31, 46]])
store.update("h",[[1, 2]],[[32, 33]])
store.update("hi",[[1, 3]],[[32, 34]])
store.update("his",[[1, 4]],[[32, 35]])
store.update("his ",[[1, 5]],[[32, 36]])
store.update("his i",[[1, 6]],[[32, 37]])
store.update("his is",[[1, 7]],[[32, 38]])
store.update("his is ",[[1, 8]],[[32, 39]])
store.update("his is e",[[1, 9]],[[32, 40]])
store.update("his is ex",[[1, 10]],[[32, 41]])
store.update("his is exa",[[1, 11]],[[32, 42]])
store.update("his is exam",[[1, 12]],[[32, 43]])
store.update("his is examp",[[1, 13]],[[32, 44]])
store.update("his is exampl",[[1, 14]],[[32, 45]])
store.update("his is example",[[1, 15]],[[32, 46]])
store.update("i",[[2, 3], [5, 6], [28, 29]],[[17, 18], [33, 34], [36, 37]])
store.update("is",[[2, 4], [5, 7], [28, 30]],[[17, 19], [33, 35], [36, 38]])
store.update("is ",[[2, 5], [5, 8], [28, 31]],[[17, 20], [33, 36], [36, 39]])
store.update("is i",[[2, 6]],[[33, 37]])
store.update("is is",[[2, 7]],[[33, 38]])
store.update("is is ",[[2, 8]],[[33, 39]])
store.update("is is e",[[2, 9]],[[33, 40]])
store.update("is is ex",[[2, 10]],[[33, 41]])
store.update("is is exa",[[2, 11]],[[33, 42]])
store.update("is is exam",[[2, 12]],[[33, 43]])
store.update("is is examp",[[2, 13]],[[33, 44]])
store.update("is is exampl",[[2, 14]],[[33, 45]])
store.update("is is example",[[2, 15]],[[33, 46]])
store.update("s",[[3, 4], [6, 7], [29, 30]],[[12, 13], [18, 19], [34, 35], [37, 38]])
store.update("s ",[[3, 5], [6, 8], [29, 31]],[[18, 20], [34, 36], [37, 39]])
store.update("s i",[[3, 6]],[[34, 37]])
store.update("s is",[[3, 7]],[[34, 38]])
store.update("s is ",[[3, 8]],[[34, 39]])
store.update("s is e",[[3, 9]],[[34, 40]])
store.update("s is ex",[[3, 10]],[[34, 41]])
store.update("s is exa",[[3, 11]],[[34, 42]])
store.update("s is exam",[[3, 12]],[[34, 43]])
store.update("s is examp",[[3, 13]],[[34, 44]])
store.update("s is exampl",[[3, 14]],[[34, 45]])
store.update("s is example",[[3, 15]],[[34, 46]])
store.update(" ",[[4, 5], [7, 8], [15, 16], [19, 20], [23, 24], [27, 28], [30, 31], [32, 33], [36, 37], [38, 39], [44, 45]],[[1, 2], [7, 8], [11, 12], [16, 17], [19, 20], [21, 22], [25, 26], [30, 31], [35, 36], [38, 39]])
store.update(" i",[[4, 6], [27, 29]],[[16, 18], [35, 37]])
store.update(" is",[[4, 7], [27, 30]],[[16, 19], [35, 38]])
store.update(" is ",[[4, 8], [27, 31]],[[16, 20], [35, 39]])
store.update(" is e",[[4, 9]],[[35, 40]])
store.update(" is ex",[[4, 10]],[[35, 41]])
store.update(" is exa",[[4, 11]],[[35, 42]])
store.update(" is exam",[[4, 12]],[[35, 43]])
store.update(" is examp",[[4, 13]],[[35, 44]])
store.update(" is exampl",[[4, 14]],[[35, 45]])
store.update(" is example",[[4, 15]],[[35, 46]])
store.update("i",[[2, 3], [5, 6], [28, 29]],[[17, 18], [33, 34], [36, 37]])
store.update("is",[[2, 4], [5, 7], [28, 30]],[[17, 19], [33, 35], [36, 38]])
store.update("is ",[[2, 5], [5, 8], [28, 31]],[[17, 20], [33, 36], [36, 39]])
store.update("is e",[[5, 9]],[[36, 40]])
store.update("is ex",[[5, 10]],[[36, 41]])
store.update("is exa",[[5, 11]],[[36, 42]])
store.update("is exam",[[5, 12]],[[36, 43]])
store.update("is examp",[[5, 13]],[[36, 44]])
store.update("is exampl",[[5, 14]],[[36, 45]])
store.update("is example",[[5, 15]],[[36, 46]])
store.update("s",[[3, 4], [6, 7], [29, 30]],[[12, 13], [18, 19], [34, 35], [37, 38]])
store.update("s ",[[3, 5], [6, 8], [29, 31]],[[18, 20], [34, 36], [37, 39]])
store.update("s e",[[6, 9]],[[37, 40]])
store.update("s ex",[[6, 10]],[[37, 41]])
store.update("s exa",[[6, 11]],[[37, 42]])
store.update("s exam",[[6, 12]],[[37, 43]])
store.update("s examp",[[6, 13]],[[37, 44]])
store.update("s exampl",[[6, 14]],[[37, 45]])
store.update("s example",[[6, 15]],[[37, 46]])
store.update(" ",[[4, 5], [7, 8], [15, 16], [19, 20], [23, 24], [27, 28], [30, 31], [32, 33], [36, 37], [38, 39], [44, 45]],[[1, 2], [7, 8], [11, 12], [16, 17], [19, 20], [21, 22], [25, 26], [30, 31], [35, 36], [38, 39]])
store.update(" e",[[7, 9], [23, 25]],[[38, 40]])
store.update(" ex",[[7, 10]],[[38, 41]])
store.update(" exa",[[7, 11]],[[38, 42]])
store.update(" exam",[[7, 12]],[[38, 43]])
store.update(" examp",[[7, 13]],[[38, 44]])
store.update(" exampl",[[7, 14]],[[38, 45]])
store.update(" example",[[7, 15]],[[38, 46]])
store.update("e",[[8, 9], [14, 15], [24, 25]],[[39, 40], [45, 46]])
store.update("ex",[[8, 10]],[[39, 41]])
store.update("exa",[[8, 11]],[[39, 42]])
store.update("exam",[[8, 12]],[[39, 43]])
store.update("examp",[[8, 13]],[[39, 44]])
store.update("exampl",[[8, 14]],[[39, 45]])
store.update("example",[[8, 15]],[[39, 46]])
store.update("x",[[9, 10]],[[40, 41]])
store.update("xa",[[9, 11]],[[40, 42]])
store.update("xam",[[9, 12]],[[40, 43]])
store.update("xamp",[[9, 13]],[[40, 44]])
store.update("xampl",[[9, 14]],[[40, 45]])
store.update("xample",[[9, 15]],[[40, 46]])
store.update("a",[[10, 11], [17, 18], [21, 22], [31, 32], [34, 35], [37, 38], [41, 42]],[[4, 5], [14, 15], [20, 21], [23, 24], [29, 30], [41, 42]])
store.update("am",[[10, 12], [21, 23]],[[41, 43]])
store.update("amp",[[10, 13]],[[41, 44]])
store.update("ampl",[[10, 14]],[[41, 45]])
store.update("ample",[[10, 15]],[[41, 46]])
store.update("m",[[11, 12], [22, 23]],[[42, 43]])
store.update("mp",[[11, 13]],[[42, 44]])
store.update("mpl",[[11, 14]],[[42, 45]])
store.update("mple",[[11, 15]],[[42, 46]])
store.update("p",[[12, 13], [39, 40]],[[2, 3], [43, 44]])
store.update("pl",[[12, 14], [39, 41]],[[2, 4], [43, 45]])
store.update("ple",[[12, 15]],[[43, 46]])
store.update("l",[[13, 14], [40, 41]],[[3, 4], [44, 45]])
store.update("le",[[13, 15]],[[44, 46]])
store.update("e",[[8, 9], [14, 15], [24, 25]],[[39, 40], [45, 46]])
store.update(" ",[[4, 5], [7, 8], [15, 16], [19, 20], [23, 24], [27, 28], [30, 31], [32, 33], [36, 37], [38, 39], [44, 45]],[[1, 2], [7, 8], [11, 12], [16, 17], [19, 20], [21, 22], [25, 26], [30, 31], [35, 36], [38, 39]])
store.update("j",[[16, 17], [20, 21]],[[0, 1], [13, 14], [27, 28]])
store.update("ja",[[16, 18], [20, 22]],[[13, 15]])
store.update("a",[[10, 11], [17, 18], [21, 22], [31, 32], [34, 35], [37, 38], [41, 42]],[[4, 5], [14, 15], [20, 21], [23, 24], [29, 30], [41, 42]])
store.update("r",[[18, 19], [47, 48]],[[10, 11]])
store.update("r ",[[18, 20]],[[10, 12]])
store.update(" ",[[4, 5], [7, 8], [15, 16], [19, 20], [23, 24], [27, 28], [30, 31], [32, 33], [36, 37], [38, 39], [44, 45]],[[1, 2], [7, 8], [11, 12], [16, 17], [19, 20], [21, 22], [25, 26], [30, 31], [35, 36], [38, 39]])
store.update("j",[[16, 17], [20, 21]],[[0, 1], [13, 14], [27, 28]])
store.update("ja",[[16, 18], [20, 22]],[[13, 15]])
store.update("a",[[10, 11], [17, 18], [21, 22], [31, 32], [34, 35], [37, 38], [41, 42]],[[4, 5], [14, 15], [20, 21], [23, 24], [29, 30], [41, 42]])
store.update("am",[[10, 12], [21, 23]],[[41, 43]])
store.update("m",[[11, 12], [22, 23]],[[42, 43]])
store.update(" ",[[4, 5], [7, 8], [15, 16], [19, 20], [23, 24], [27, 28], [30, 31], [32, 33], [36, 37], [38, 39], [44, 45]],[[1, 2], [7, 8], [11, 12], [16, 17], [19, 20], [21, 22], [25, 26], [30, 31], [35, 36], [38, 39]])
store.update(" e",[[7, 9], [23, 25]],[[38, 40]])
store.update("e",[[8, 9], [14, 15], [24, 25]],[[39, 40], [45, 46]])
store.update("c",[[25, 26], [33, 34]],[[22, 23]])
store.update("t",[[0, 1], [26, 27], [35, 36]],[[24, 25], [31, 32]])
store.update("t ",[[26, 28], [35, 37]],[[24, 26]])
store.update(" ",[[4, 5], [7, 8], [15, 16], [19, 20], [23, 24], [27, 28], [30, 31], [32, 33], [36, 37], [38, 39], [44, 45]],[[1, 2], [7, 8], [11, 12], [16, 17], [19, 20], [21, 22], [25, 26], [30, 31], [35, 36], [38, 39]])
store.update(" i",[[4, 6], [27, 29]],[[16, 18], [35, 37]])
store.update(" is",[[4, 7], [27, 30]],[[16, 19], [35, 38]])
store.update(" is ",[[4, 8], [27, 31]],[[16, 20], [35, 39]])
store.update(" is a",[[27, 32]],[[16, 21]])
store.update(" is a ",[[27, 33]],[[16, 22]])
store.update(" is a c",[[27, 34]],[[16, 23]])
store.update(" is a ca",[[27, 35]],[[16, 24]])
store.update(" is a cat",[[27, 36]],[[16, 25]])
store.update(" is a cat ",[[27, 37]],[[16, 26]])
store.update("i",[[2, 3], [5, 6], [28, 29]],[[17, 18], [33, 34], [36, 37]])
store.update("is",[[2, 4], [5, 7], [28, 30]],[[17, 19], [33, 35], [36, 38]])
store.update("is ",[[2, 5], [5, 8], [28, 31]],[[17, 20], [33, 36], [36, 39]])
store.update("is a",[[28, 32]],[[17, 21]])
store.update("is a ",[[28, 33]],[[17, 22]])
store.update("is a c",[[28, 34]],[[17, 23]])
store.update("is a ca",[[28, 35]],[[17, 24]])
store.update("is a cat",[[28, 36]],[[17, 25]])
store.update("is a cat ",[[28, 37]],[[17, 26]])
store.update("s",[[3, 4], [6, 7], [29, 30]],[[12, 13], [18, 19], [34, 35], [37, 38]])
store.update("s ",[[3, 5], [6, 8], [29, 31]],[[18, 20], [34, 36], [37, 39]])
store.update("s a",[[29, 32]],[[18, 21]])
store.update("s a ",[[29, 33]],[[18, 22]])
store.update("s a c",[[29, 34]],[[18, 23]])
store.update("s a ca",[[29, 35]],[[18, 24]])
store.update("s a cat",[[29, 36]],[[18, 25]])
store.update("s a cat ",[[29, 37]],[[18, 26]])
store.update(" ",[[4, 5], [7, 8], [15, 16], [19, 20], [23, 24], [27, 28], [30, 31], [32, 33], [36, 37], [38, 39], [44, 45]],[[1, 2], [7, 8], [11, 12], [16, 17], [19, 20], [21, 22], [25, 26], [30, 31], [35, 36], [38, 39]])
store.update(" a",[[30, 32], [36, 38]],[[19, 21]])
store.update(" a ",[[30, 33], [36, 39]],[[19, 22]])
store.update(" a c",[[30, 34]],[[19, 23]])
store.update(" a ca",[[30, 35]],[[19, 24]])
store.update(" a cat",[[30, 36]],[[19, 25]])
store.update(" a cat ",[[30, 37]],[[19, 26]])
store.update("a",[[10, 11], [17, 18], [21, 22], [31, 32], [34, 35], [37, 38], [41, 42]],[[4, 5], [14, 15], [20, 21], [23, 24], [29, 30], [41, 42]])
store.update("a ",[[31, 33], [37, 39]],[[20, 22], [29, 31]])
store.update("a c",[[31, 34]],[[20, 23]])
store.update("a ca",[[31, 35]],[[20, 24]])
store.update("a cat",[[31, 36]],[[20, 25]])
store.update("a cat ",[[31, 37]],[[20, 26]])
store.update(" ",[[4, 5], [7, 8], [15, 16], [19, 20], [23, 24], [27, 28], [30, 31], [32, 33], [36, 37], [38, 39], [44, 45]],[[1, 2], [7, 8], [11, 12], [16, 17], [19, 20], [21, 22], [25, 26], [30, 31], [35, 36], [38, 39]])
store.update(" c",[[32, 34]],[[21, 23]])
store.update(" ca",[[32, 35]],[[21, 24]])
store.update(" cat",[[32, 36]],[[21, 25]])
store.update(" cat ",[[32, 37]],[[21, 26]])
store.update("c",[[25, 26], [33, 34]],[[22, 23]])
store.update("ca",[[33, 35]],[[22, 24]])
store.update("cat",[[33, 36]],[[22, 25]])
store.update("cat ",[[33, 37]],[[22, 26]])
store.update("a",[[10, 11], [17, 18], [21, 22], [31, 32], [34, 35], [37, 38], [41, 42]],[[4, 5], [14, 15], [20, 21], [23, 24], [29, 30], [41, 42]])
store.update("at",[[34, 36]],[[23, 25]])
store.update("at ",[[34, 37]],[[23, 26]])
store.update("t",[[0, 1], [26, 27], [35, 36]],[[24, 25], [31, 32]])
store.update("t ",[[26, 28], [35, 37]],[[24, 26]])
store.update(" ",[[4, 5], [7, 8], [15, 16], [19, 20], [23, 24], [27, 28], [30, 31], [32, 33], [36, 37], [38, 39], [44, 45]],[[1, 2], [7, 8], [11, 12], [16, 17], [19, 20], [21, 22], [25, 26], [30, 31], [35, 36], [38, 39]])
store.update(" a",[[30, 32], [36, 38]],[[19, 21]])
store.update(" a ",[[30, 33], [36, 39]],[[19, 22]])
store.update("a",[[10, 11], [17, 18], [21, 22], [31, 32], [34, 35], [37, 38], [41, 42]],[[4, 5], [14, 15], [20, 21], [23, 24], [29, 30], [41, 42]])
store.update("a ",[[31, 33], [37, 39]],[[20, 22], [29, 31]])
store.update(" ",[[4, 5], [7, 8], [15, 16], [19, 20], [23, 24], [27, 28], [30, 31], [32, 33], [36, 37], [38, 39], [44, 45]],[[1, 2], [7, 8], [11, 12], [16, 17], [19, 20], [21, 22], [25, 26], [30, 31], [35, 36], [38, 39]])
store.update(" p",[[38, 40]],[[1, 3]])
store.update(" pl",[[38, 41]],[[1, 4]])
store.update(" pla",[[38, 42]],[[1, 5]])
store.update(" plan",[[38, 43]],[[1, 6]])
store.update(" plank",[[38, 44]],[[1, 7]])
store.update(" plank ",[[38, 45]],[[1, 8]])
store.update(" plank f",[[38, 46]],[[1, 9]])
store.update(" plank fo",[[38, 47]],[[1, 10]])
store.update(" plank for",[[38, 48]],[[1, 11]])
store.update("p",[[12, 13], [39, 40]],[[2, 3], [43, 44]])
store.update("pl",[[12, 14], [39, 41]],[[2, 4], [43, 45]])
store.update("pla",[[39, 42]],[[2, 5]])
store.update("plan",[[39, 43]],[[2, 6]])
store.update("plank",[[39, 44]],[[2, 7]])
store.update("plank ",[[39, 45]],[[2, 8]])
store.update("plank f",[[39, 46]],[[2, 9]])
store.update("plank fo",[[39, 47]],[[2, 10]])
store.update("plank for",[[39, 48]],[[2, 11]])
store.update("l",[[13, 14], [40, 41]],[[3, 4], [44, 45]])
store.update("la",[[40, 42]],[[3, 5]])
store.update("lan",[[40, 43]],[[3, 6]])
store.update("lank",[[40, 44]],[[3, 7]])
store.update("lank ",[[40, 45]],[[3, 8]])
store.update("lank f",[[40, 46]],[[3, 9]])
store.update("lank fo",[[40, 47]],[[3, 10]])
store.update("lank for",[[40, 48]],[[3, 11]])
store.update("a",[[10, 11], [17, 18], [21, 22], [31, 32], [34, 35], [37, 38], [41, 42]],[[4, 5], [14, 15], [20, 21], [23, 24], [29, 30], [41, 42]])
store.update("an",[[41, 43]],[[4, 6]])
store.update("ank",[[41, 44]],[[4, 7]])
store.update("ank ",[[41, 45]],[[4, 8]])
store.update("ank f",[[41, 46]],[[4, 9]])
store.update("ank fo",[[41, 47]],[[4, 10]])
store.update("ank for",[[41, 48]],[[4, 11]])
store.update("n",[[42, 43]],[[5, 6]])
store.update("nk",[[42, 44]],[[5, 7]])
store.update("nk ",[[42, 45]],[[5, 8]])
store.update("nk f",[[42, 46]],[[5, 9]])
store.update("nk fo",[[42, 47]],[[5, 10]])
store.update("nk for",[[42, 48]],[[5, 11]])
store.update("k",[[43, 44]],[[6, 7]])
store.update("k ",[[43, 45]],[[6, 8]])
store.update("k f",[[43, 46]],[[6, 9]])
store.update("k fo",[[43, 47]],[[6, 10]])
store.update("k for",[[43, 48]],[[6, 11]])
store.update(" ",[[4, 5], [7, 8], [15, 16], [19, 20], [23, 24], [27, 28], [30, 31], [32, 33], [36, 37], [38, 39], [44, 45]],[[1, 2], [7, 8], [11, 12], [16, 17], [19, 20], [21, 22], [25, 26], [30, 31], [35, 36], [38, 39]])
store.update(" f",[[44, 46]],[[7, 9], [25, 27]])
store.update(" fo",[[44, 47]],[[7, 10]])
store.update(" for",[[44, 48]],[[7, 11]])
store.update("f",[[45, 46]],[[8, 9], [26, 27]])
store.update("fo",[[45, 47]],[[8, 10]])
store.update("for",[[45, 48]],[[8, 11]])
store.update("o",[[46, 47]],[[9, 10]])
store.update("or",[[46, 48]],[[9, 11]])
store.update("r",[[18, 19], [47, 48]],[[10, 11]])

print(store)



store.removeRedundantPairs()
print(store)


store.removeUnderlaps()
store.filter()

store.getADataStream()
print("------")
store.getBDataStream()


#print(store)
#store.cleanEmpty()
#print(store)
