

def find_matching_substrings(string1, string2, case_sensitive=False):
    if not case_sensitive:
        string1 = string1.lower()
        string2 = string2.lower()
    matching_substrings = []
    for i in range(len(string1)):
        for j in range(i+1, len(string1)+1):
            if string1[i:j] in string2 and string1[i:j] not in matching_substrings:
                matching_substrings.append(string1[i:j])
    return matching_substrings


def findTokens(inputA, inputB,caseSensative):
    identifiedTokens = []

    if caseSensative:
        inputA = inputA.lower()
        inputB = inputB.lower()    
    for x in range(len(inputA)):
        for y in range(x+1,len(inputA)+1):
            subString = inputA[x:y]
            if subString in inputB:
                identifiedTokens.append(subString)

    return list(identifiedTokens)



#print(find_matching_substrings("this is here","This"))
print(findTokens("this is here","This",True))
print(findTokens("this is here","This",False))