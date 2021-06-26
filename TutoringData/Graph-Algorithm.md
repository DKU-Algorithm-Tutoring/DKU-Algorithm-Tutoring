## :star: 그래프 이론

### 이미 배운 내용 복습

그래프를 다루는 내용들을 복습해보자. 처음 그래프를 접한건 5장 `DFS/BFS` 알고리즘이다. 그리고 바로 전에 배운 `최단 경로`에서 다룬 내용은 모두 그래프 알고리즘의 한 유형으로 볼 수 있다. 이외에도 그래프 알고리즘은 굉장히 다양한데, 코딩 테스트에서 출제 비중이 낮은 편이지만 꼭 제대로 알아야 하는 알고리즘이다.

내용을 다루기 전에, 앞서 공부했던 그래프에 대해 복습해보면, 먼저 `그래프`란 `노드`와 `노드` 사이에 연결된 `간선`의 정보를 가지고 있는 자료구조를 의미한다. 알고리즘 문제를 접했을 때 **서로 다른 개체(혹은 객체)**가 연결되어 있다는 이야기를 들으면 가장 먼저 그래프 알고리즘을 떠올려야 한다. 더불어 그래프 자료구조 중에서 `트리` 자료구조는 다양한 알고리즘에서 사용되므로 꼭 기억해야 한다. 참고로 트리는 전통적인 수학에서는 무방향 그래프로 간주되지만, 컴퓨터공학 분야에서는 보통 방향 그래프라고 간주된다.

특징 | 그래프 | 트리
:---: | :---: | :---:
방향성 | 방향 그래프 혹은 무방향 그래프 | 방향 그래프
순환성 | 순환 및 비순환 | 비순환
루트 노드 존재 여부 | 루트 노드가 없음 | 루트 노드가 존재
노드간 관계성 | 부모와 자식 관계 없음 | 부모와 자식 관계
모델의 종류 | 네트워크 모델 | 계층 모델


또한 그래프의 구현 방법은 2가지의 방식이 존재한다.

- 인접 행렬 : 2차원 배열을 사용하는 방식
- 인접 리스트 : 리스트를 사용하는 방식

2가지 모두 그래프 알고리즘에서 매우 많이 사용된다. 두 방식은 메모리와 속도 측면에서 구별되는 특징을 가진다는 점을 기억하자. 노드의 개수가 V, 간선의 개수가 E인 그래프를 생각해보면, 인접 행렬을 이용하는 방식은 간선 정보를 저장하기 위해서 O(V<sup>2</sup>)만큼의 메모리 공간이 필요하다. 반면에 인접 리스트를 이용할 때는 간선의 개수만큼인 O(E)만큼만 메모리 공간이 필요하다. 또한 인접 행렬은 특정한 노드 A에서 다른 특정한 노드 B로 이어진 간선의 비용은 O(1)의 시간으로 즉시 알 수 있다는 장점이 있으며, 반면에 인접 리스트를 이용할 때는 O(V)만큼의 시간이 소요된다.

 ### 서로소 집합

수학에서 `서로소 집합`이란 **공통 원소가 없는 두 집합**을 의미한다. 서로소 집합 자료구조를 설명하려면 서로소 집합 개념이 필요하다. 서로소 집합 자료구조는 몇몇 그래프 알고리즘에서 매우 중요하게 사용된다. `서로소 집합 자료구조`란 **서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조**라고 할 수 있다. 서로소 집합 자료구조는 `union`과 `find` 2개의 연산으로 조작할 수 있다.

union 연산은 **2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산**이다. find 연산은 **특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산**이다. 서로소 집합 자료구조는 union-find 자료구조라고 불리기도 한다.

 ### 서로소 집합 자료구조

서로소 집합 자료구조를 구현할 때는 `트리 자료구조`를 이용하여 집합을 표현하는데, 서로소 집합 정보가 주어졌을 때 트리 자료구조를 이용해서 집합을 표현하는 서로소 집합 계산 알고리즘은 다음과 같다.

- union 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다.
    - A와 B의 루트 노드 A, B를 각각 찾는다.
    - A를 B의 부모 노드로 설정한다(B가 A를 가리키도록)
- 모든 union 연산을 처리할 때까지 위의 과정을 반복한다.

`기본적인 서로소 집합 알고리즘`

```
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)

for i in range(N + 1):
    parent[i] = i

for i in range(M):
    A, B = map(int, input().split())
    union_parent(parent, A, B)

print('각 원소가 속한 집합 : ', end=' ')
for i in range(1, N + 1):
    print(find_parent(parent, i), end=' ')
print()

print('부모 테이블: ', end=' ')
for i in range(1, N + 1):
    print(parent[i], end=' ')
```

`경로 압축 기법`

```
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
```

`개선된 서로소 집합 알고리즘`

```
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)

for i in range(N + 1):
    parent[i] = i

for i in range(M):
    A, B = map(int, input().split())
    union_parent(parent, A, B)

print('각 원소가 속한 집합 : ', end=' ')
for i in range(1, N + 1):
    print(find_parent(parent, i), end=' ')
print()

print('부모 테이블: ', end=' ')
for i in range(1, N + 1):
    print(parent[i], end=' ')
```

### 서로소 집합을 활용한 사이클 판별

서로소 집합은 다양한 알고리즘에 사용될 수 있다. 특히 **서로소 집합은 무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있다는 특징이 있다.** 참고로 방향 그래프에서의 사이클 여부는 `DFS`를 이용하여 판별할 수 있다. 사이클을 판별한는 알고리즘은 다음과 같다.

- 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
    - 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산을 수행한다.
    - 루트 노드가 서로 같다면 사이클이 발생한 것이다.
- 그래프에 포함되어 있는 모든 간선에 대하여 위의 과정을 반복한다.

`서로소 집합을 활용한 사이클 판별`

```
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


V, E = map(int, input().split())
parent = [0] * (V + 1)
cycle = False

for i in range(1, V + 1):
    parent[i] = i

for i in range(E):
    A, B = map(int, input().split())
    if find_parent(parent, A) == find_parent(parent, B):
        cycle = True
        break
    else:
        union_parent(parent, A, B)

if cycle:
    print('cycle이 일어났습니다.')
else:
    print('cucle이 일어나지 않았습니다.')
```

### 신장 트리

신장 트리는 그래프 알고리즘 문제로 자주 출제되는 문제 유형이다. 기본적으로 `신장 트리`란 **하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프**를 의미한다. 이때 모든 노드가 포함되어 서로 연결되면서 **사이클이 존재하지 않는다는 조건은 트리의 성립 조건**이기도 하다. 그래서 이러한 그래프를 신장 트리라고 부르는 것이다. 신장 트리 중에서 최소 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘을 `최소 신장 트리 알고리즘`이라고 한다. 대표적인 최소 신장 트리 알고리즘으로는 `크루스칼 알고리즘`이 있다.

### 크루스칼 알고리즘

크루스칼 알고리즘을 사용하면 가장 적은 비용으로 모든 노드를 연결할 수 있는데 크루스칼 알고리즘은 그리디 알고리즘으로 분류된다. **먼저 모든 간선에 대하여 정렬을 수행한 뒤에 가장 거리가 짧은 간선부터 집합에 포함시키면 된다.** 이때 사이클을 발생시킬 수 있는 간선의 경우, 집합에 포함시키지 않는다. 구체적인 알고리즘을 살펴보면 다음과 같다.

- 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
- 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
    - 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다.
    - 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
- 모든 간선에 대하여 2번째 과정을 반복한다.

`크루스칼 알고리즘`

```
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


V, E = map(int, input().split())
parent = [0] * (V + 1)
edges = []
result = 0

for i in range(1, V + 1):
    parent[i] = i

for i in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    Cost, A, B = edge
    if find_parent(parent, A) != find_parent(parent, B):
        union_parent(parent, A, B)
        result += Cost

print(result)
```

### 위상 정렬

`위상 정렬`은 정렬 알고리즘의 일종이다. 위상 정렬은 **순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘**이다. 조금 더 이론적으로 설명하자면, 위상 정렬이란 **방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것**이다. 현실 세계에서 위상 정렬을 수행하게 되는 전형적인 예시로는 **선수과목을 고려한 학습 순서 설정**을 들 수 있다. 위상 정렬의 알고리즘은 다음과 같다.

- 진입차수가 0인 노드를 큐에 넣는다.
- 큐가 빌 때까지 다음의 과정을 반복한다.
    - 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
    - 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
- 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단할 수 있다.

`위상 정렬 알고리즘`

```
from collections import deque

V, E = map(int, input().split())

indegree = [0] * (V + 1)
graph = [[] for i in range(V + 1)]

for i in range(E):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1


def topology_sort():
    result = []
    queue = deque()

    for i in range(1, V + 1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        now = queue.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

    for i in result:
        print(i, end=' ')
```