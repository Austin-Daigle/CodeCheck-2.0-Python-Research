def findSharedPatterns(a, b):
    result = []
    
    for i in range(len(a)):
        for j in range(len(b)):
            # Check if the current elements match
            if a[i] == b[j]:
                # Initialize the shared pattern and indices
                sharedPattern = [a[i]]
                aIndices = [i, i]
                bIndices = [j, j]
                
                # Check for matching subsequent elements
                k = 1
                while i + k < len(a) and j + k < len(b) and a[i + k] == b[j + k]:
                    sharedPattern.append(a[i + k])
                    aIndices[1] = i + k
                    bIndices[1] = j + k
                    k += 1
                
                # If the pattern is longer than 1 element, add it to the result
                if len(sharedPattern) > 1:
                    result.append([sharedPattern, aIndices, bIndices])
    


    return result

a = ['this ', ' is here','this ', ' a demo', 'this ', ' is here', ' cat', ' this ', ' is here']
b = ['this ', ' is here', ' dork', 'this ', 'cookie ', 'this ', ' is here','this ', ' a demo']

findSharedPatterns(a, b)

