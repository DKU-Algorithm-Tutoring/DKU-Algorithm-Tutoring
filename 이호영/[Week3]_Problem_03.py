n = int(input())
num = []
for i in range(n):
    x = int(input())
    if x > 0:
        num.append(x)
    elif x == 0:
        if len(num)==0:
            print("0")
        else:
            print(min(num))
            num.pop(num.index(min(num)))
