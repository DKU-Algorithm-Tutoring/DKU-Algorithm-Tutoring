from itertools import combinations

L, C = map(int, input().split()) # {4, 6}
data = set(input().split()) # {a, t, c, i, s, w}

A = set(['a', 'e', 'i', 'o', 'u'])

word_list = data & A # {a, i}

for i in combinations(sorted(data), L):
    num = len(set(i) & word_list)
    if num == 0 or L - num < 2: continue
    print(''.join(i))
