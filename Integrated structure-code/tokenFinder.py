
def matched_substrings2(string1, string2):
    matched_subs = []
    for i in range(len(string1)):
        for j in range(i + 1, len(string1) + 1):
            substring = string1[i:j]
            if substring in string2:
                matched_subs.append(substring)
    return matched_subs



def matched_substrings(string1, string2,isCaseSensative):
    matched_subs = []
    for i in range(len(string1)):
        for j in range(i + 1, len(string1) + 1):
            substring = string1[i:j]   
            if isCaseSensative:
                if substring in string2:
                    matched_subs.append(substring)
            else:
                if substring.lower() in string2.lower():
                    matched_subs.append(substring)
    return list(set(matched_subs))

tokens = matched_substrings("this is eat","this is that",True)
print(tokens)
print(len(tokens))
