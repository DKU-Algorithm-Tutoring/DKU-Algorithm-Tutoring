N = int(input())
for i in range(N):
    N_list = list(map(int, input()))
New_list = []
for x in N_list:
    if x == 0:
        if not New_list:
            print(0)
        else:
            print(min(New_list))
            New_list.remove(min(New_list))
    else:
        New_list.append(x)
