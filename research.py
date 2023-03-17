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
        result.append([currentPosition,currentPosition+len(token)])
        startPosition = currentPosition + 1
    return result

def compileTokenData(inputA,inputB,isCaseSensative):
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
        #print(items,"\t",findAllTokenIndexes(inputA,items),"\t\t",findAllTokenIndexes(inputB,items))
        print("store.update(\""+str(items)+"\","+str(findAllTokenIndexes(inputA,items))+","+str(findAllTokenIndexes(inputB,items))+")")

############################################

compileTokenData("this is here","This",True)
