n=int(input())
for _ in range(n):
    a, b = map(int, input().split())
    lst = list(map(int, input().split()))
    count = 1
    while True:
        if lst[0] != max(lst):
            save = lst[0]
            lst.pop(0)
            lst.append(save)
            if b == 0:
                b = len(lst) - 1
            else:
                b = b - 1
        else:
            lst.pop(0)
            if b == 0:
                 print(count)
                 break
            else:
                 count += 1
                 b -= 1