from itertools import combinations

n,m = map(int, input().split())
num_list = list(map(int, input().split()))
count = 0

for i in range(1, len(num_list)+1):
    c = list(combinations(num_list, i))

    for j in c:
        if sum(j) == m:
            count += 1

print(count)
