def get_matching_patterns(a, b):
    # initialize empty result list
    result = []

    # loop through each string in a
    for i in range(len(a)):
        # loop through each string in b
        for j in range(len(b)):
            # if the strings match, find the sequence of matching patterns
            if a[i] == b[j]:
                # initialize variables to store the beginning and ending indexes of the pattern
                start_a = i
                start_b = j
                end_a = i
                end_b = j

                # loop through the remaining strings in a and b, looking for the next matching patterns
                while end_a < len(a)-1 and end_b < len(b)-1 and a[end_a+1] == b[end_b+1]:
                    end_a += 1
                    end_b += 1

                # check if the pattern has two or more matching strings
                if end_a - start_a >= 1 and end_b - start_b >= 1:
                    # add the pattern to the result list
                    result.append([[[start_a, end_a]],[[start_b, end_b]],a[start_a:end_a+1]])
                #"".join('\''+x+'\'' for x in a[start_a:end_a+1])
    return result

#----------------------------------------------------------

"""
a = [[[0, 5], 'this '], [[7, 15], ' a demo '], [[15, 20], 'this '], [[19, 28], ' is here '], [[36, 41], 'this '], [[42, 51], ' is here '], [[50, 56], ' aliens'], [[57, 63], ' have '], [[66, 73], ' landed']]
b = [[[0, 5], 'this '], [[10, 19], ' is here '], [[22, 30], ' a demo '], [[29, 35], ' aliens'], [[36, 42], ' have '], [[41, 48], ' landed']]


a = [[[0, 16], 'the red kangaroo'], [[16, 41], ' is the largest marsupial'], [[45, 48], ' ca'], [[49, 54], ' jump'], [[54, 88], ' up to three times its own height.']]
b = [[[29, 45], 'the red kangaroo'], [[52, 77], ' is the largest marsupial'], [[81, 84], ' ca'], [[92, 97], ' jump'], [[100, 134], ' up to three times its own height.']]

"""

a = [[[0, 5], 'this '],
[[7, 14], ' a demo'],
[[15, 20], 'this '],
[[19, 27], ' is here'],
[[40, 43], ' cat'],
[[70, 74], ' this '],
[[90, 97], ' is here']]


b = [[[0, 5], 'this '],
[[10, 18], ' is here'],
[[50, 54], ' dork'],
[[60, 65], 'this '],
[[100, 107], 'cookie '],
[[100, 107], 'this '],
[[110, 117], ' is here']]

#---------------------------



#---------------------------




#print([x[1] for x in a])
#print([x[1] for x in b])
print("")
result = get_matching_patterns([x[1] for x in a], [x[1] for x in b])

for x in result:
    print(x)







