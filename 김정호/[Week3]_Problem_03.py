n=int(input())
qoduf=[]
for _ in range(n):
     x=int(input())
     if x==0:
        if len(qoduf)==0:
            print('0')
        else:
            mini=min(qoduf)
            print(mini)
            qoduf.remove(mini)
     else:
        qoduf.append(x)