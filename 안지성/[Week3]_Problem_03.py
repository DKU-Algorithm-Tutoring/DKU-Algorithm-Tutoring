list1 = [0]

N = int(input()) # N(1 ≤ N ≤ 100,000)
r = 0
while(r < N):
    x = int(input())

    if list1:
        smallest = list1[0]
        for i in list1:
            if i < smallest:
                smallest = i

    if x == 0:
        if list1:
            print(smallest)
            list1.remove(list1.index(smallest))
        else:
            print(0)

    elif x>0:
        list1.append(x)
