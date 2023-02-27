 
#######################################
# return all index pairs of the 
# given token within a string 
# to search.
#######################################
def findAllTokenIndexes(string,token):
    # by default case sensativity is respected by default
    isCaseSensative = True
    result = []
    #result.append(token)
    startPosition = 0
    while startPosition < len(string):
        if(isCaseSensative):
            currentPosition = string.find(token, startPosition)
        else:
            currentPosition = string.lower().find(token.lower(), startPosition)
        if currentPosition == -1:
            break
        result.append([currentPosition,currentPosition+len(token)])
        startPosition = currentPosition + 1
    return result

#######################################
# this method returns all of the 
# raw, unfiltered tokens shared between
# two strings within the parameters
#######################################
def findTokens(inputA, inputB):
    identifiedTokens = []
    for x in range(len(inputA)):
        for y in range(x+1,len(inputA)+1):
            subString = inputA[x:y]
            if subString in inputB:
                identifiedTokens.append(subString)

    return list(identifiedTokens)

#######################################
# ["token",[a,b],[c,d],[e,f],...,[...,...]]
#######################################

def getTokens(inputA, inputB, isCaseSensative):
    tokens = findTokens(inputA, inputB)
    print("=========================================================")
    print("InputA: \""+str(inputA)+"\"")
    print("InputB: \""+str(inputB)+"\"")
    print("")
    print("*** All Identified Tokens shared between inputA and inputB ***")
    print("=========================================================")
    print(tokens)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #filter tokens list here using filter parameters
    print("Token Index Data Printout for INPUT A")
    inputATokenIndexDatabase = []
    for x in range(0,len(tokens)):
        inputATokenIndexDatabase.append(findAllTokenIndexes(inputA,tokens[x]))
    for x in range(0,len(inputATokenIndexDatabase)):
        print(tokens[x])
        print(inputATokenIndexDatabase[x])
        
    print("")
    print("Token Index Data Printout for INPUT B")
    inputBTokenIndexDatabase = []
    for x in range(0,len(tokens)):
        inputBTokenIndexDatabase.append(findAllTokenIndexes(inputB,tokens[x]))
    for x in range(0,len(inputBTokenIndexDatabase)):
        print(tokens[x])
        print(inputBTokenIndexDatabase[x])
############################################

getTokens("This is here","This",True)

