from itertools import combinations
L, C = map(int,input().split(','))
S = list(map(str,input().split()))
S = sorted(S)
result = list(combinations(S, 4))
print(result)