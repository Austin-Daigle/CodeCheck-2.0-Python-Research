def find_sequential_patterns(a, b):
    patterns = []
    for i in range(len(a)-1):
        pattern = [a[i], a[i+1]]
        if pattern in patterns:
            continue
        if pattern in [b[j:j+2] for j in range(len(b)-1)]:
            patterns.append(pattern)
    return patterns

a = ['this ', ' a demo', 'this ', ' is here', ' cat', ' this ', ' is here']
b = ['this ', ' is here', ' dork', 'this ', 'cookie ', 'this ', ' is here']

patterns = find_sequential_patterns(a, b)
print(patterns)