n,m=map(int,input().split())
lst=list(map(int,input().split()))
up=0
down=0
count=0
def adder(u,d):
     total=0
     for i in range(u,d+1):
        total+=lst[i]
     return total
while up!=n-1 and down!=n-1:
     z=adder(up, down)
     if z==m:
        count+=1
     elif z<m:
        down+=1
        if down==n:
            down-=1
            up+=1
     else:
        up+=1
        if up==n:
            up-=1
            down+=1
print(count)