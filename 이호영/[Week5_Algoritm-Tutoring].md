# 1
<그림 1>과 같이 정사각형 모양의 지도가 있다.
1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
대각선상에 집이 있는 경우는 연결된 것이 아니다.
<그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여
출력하는 프로그램을 작성하시오.

```python
from collections import deque
n = int(input())
graph = []
count = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(n):
    graph.append(list(map(int,input())))

def apt(x,y):
    que = deque()
    que.append((x,y))
    j = 0
    count = [0]
    while que:
        x,y = que.popleft()
        if graph[x][y] == 1 or graph[x][y]==2:
            if graph[x][y]==1:
                count[0] += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 or ny<0 or nx>=n or ny>=len(graph[0]):
                    continue
                if graph[nx][ny]==0:
                    continue
                if graph[nx][ny]==1:
                        que.append((nx,ny))
                        graph[x][y]=2
                        graph[nx][ny]=2
                        count[0]+=1

    return count
result = 0
for k in range(n):
    for l in range(len(graph[0])):
        count.append(apt(k,l))
for a in range(len(count)):
    count = [i for i in count if not 0 in i]
count.sort()

print(len(count))
for a in range(len(count)):
    print(count[a][0])

```
# 2
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다.
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자.
1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어
2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.
어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다.
컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

``` python
from collections import deque
import sys
n = int(input())
m = int(input())
com = []
graph = [[0]]
visited = [False] * (n+1)


for i in range(m):
    co = list(map(int,sys.stdin.readline().split()))
    com.append(co)
for j in range(m):
    com[j].sort
for k in range(n):
    graph.append([])
    for l in range(m):
        if k+1 in com[l]:
            if k+1==com[l][0]:
                graph[k+1].append(com[l][1])
            else:
                graph[k + 1].append(com[l][0])


def bfs(Graph, s, Visited):
    queue = deque([s])
    Visited[s] = True
    count = 0
    while queue:
        v = queue.popleft()
        count+=1

        for i in Graph[v]:
            if Visited[i] is False:
                queue.append(i)
                Visited[i] = True
    return count


result=bfs(graph, 1, visited)
print(result-1)
```

# 3
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
``` python
from collections import deque
import sys
n,m = map(int, input().split())

com = []
graph = [[0]]
visited = [False] * (n+1)
count = 0
for i in range(m):
    co = list(map(int,sys.stdin.readline().split()))
    com.append(co)
for j in range(m):
    com[j].sort
for k in range(n):
    graph.append([])
    for l in range(m):
        if k+1 in com[l]:
            if k+1==com[l][0]:
                graph[k+1].append(com[l][1])
            else:
                graph[k + 1].append(com[l][0])
def bfs(Graph, s, Visited):
    queue = deque([s])
    Visited[s] = True
    while queue:
        v = queue.popleft()
        for i in Graph[v]:
            if Visited[i] is False:
                queue.append(i)
                Visited[i] = True

for o in range(n):
    if visited[o+1] is False:
        bfs(graph, o+1, visited)
        count+=1
print(count)
```

# 4
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.
한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 
두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다.
지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

``` python
from collections import deque
graph = []
dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,1,-1,-1,1]
def apt(y,x):
    que = deque()
    que.append((x,y))
    if graph[x][y]== 0:
        return False
    while que:
        x,y = que.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                    que.append((nx,ny))
                    graph[x][y]=0
                    graph[nx][ny]=0
    return True
while True:
    n, m = map(int, input().split())
    count = 0
    graph = []
    if n==0 and m==0:
        exit(0)
    for _ in range(m):
        graph.append(list(map(int,input().split())))
    for h in range(m):
        for w in range(n):
            result=apt(w,h)
            if result == True:
                count += 1
    print(count)
```
