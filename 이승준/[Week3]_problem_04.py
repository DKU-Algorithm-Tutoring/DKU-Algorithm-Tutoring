from itertools import combinations
N, M = map(int, input().split())
N_list = list(map(int,input().split()))
count = 0
for i in range(1, N):
    list_p = list(combinations(N_list, i))
    for j in range(len(list_p)):
        list_sum = 0
        list_sum = sum(list_p[ j])
        if(list_sum == M):
            count = count+1
print(count)