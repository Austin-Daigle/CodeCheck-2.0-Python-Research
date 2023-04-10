def find_patterns(a, b):
    n = len(a)
    m = len(b)
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    patterns = []
    i = n
    j = m
    current_pattern = []

    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            current_pattern.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            if len(current_pattern) >= 2:
                patterns.append(tuple(reversed(current_pattern)))
            current_pattern = []
            i -= 1
        else:
            if len(current_pattern) >= 2:
                patterns.append(tuple(reversed(current_pattern)))
            current_pattern = []
            j -= 1

    if len(current_pattern) >= 2:
        patterns.append(tuple(reversed(current_pattern)))

    return patterns

a = ['this ', ' a demo', 'this ', ' is here', ' cat', ' this ', ' is here','adxada', 'candy', 'store']
b = ['this ', ' is here', 'candy', 'store', ' dork', 'this ', 'cookie ', 'this ', ' is here']

patterns = find_patterns(a, b)
print(patterns)
