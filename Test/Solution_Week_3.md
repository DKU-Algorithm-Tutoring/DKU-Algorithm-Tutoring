## :star: 3주차 문제

한문제당 100점 만점이며 검색은 알고리즘에 관한 검색은 허용하나, 답지를 보는 행위는 시험이 끝나고 해주세요. 또한 이 문제를 가지고 다음주 발표를 진행할 예정이니 자신이 이해하고 잘 설명할 수 있는 문제를 하나 뽑아주세요. 이번주 과제는 백준 Class 1을 모두 끝내주세요. 

문제는 전부 백준에서 참고했습니다.

### :speech_balloon: Problem
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.

### :warning: Limit
첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.

### input

```
8
4
3
6
8
7
5
2
1
```

### output
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.

```
+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-
```

### :computer: Code

```
n = int(input())

stack = []
result = []
origin_array = []
push_array = []
stack_number = 1

for _ in range(n):
    number = int(input())
    origin_array.append(number)

    while stack_number <= number:
        stack.append(stack_number)
        stack_number += 1
        result.append('+')
    if stack[-1] == number:
        push_array.append(stack.pop())
        result.append('-')

if push_array == origin_array:
    [print(x) for x in result]
else:
    print('NO')
```

### 📝 Solution
우선 시간 제한은 2초 즉 계산한 시간복잡도가 2억번 이하면 된다. 문제를 살펴보면 stack은 오름차순으로 정렬되어 있다고 가정을 한다. 그래서 처음부터 숫자를 넣을 필요는 없고 입력되는 숫자에 따라서 넣어주면 된다. 또한 스택은 LIFO 특성이 있기 때문에 꺼내려는 숫자가 마지막 인덱스가 가리키는 숫자면 꺼내어준다. 그리고 마지막으로 내가 꺼낸 숫자와 본래의 숫자가 맞으면 '+', '-' 연산이 들어 가 있는 result 배열을 꺼내면 되고 아니면 NO를 출력하면 된다.

### :speech_balloon: Problem
여러분도 알다시피 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 ‘순서대로’, 즉 먼저 요청된 것을 먼저 인쇄한다. 여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO - First In First Out - 에 따라 인쇄가 되게 된다. 하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.

현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.

### :warning: Limit
첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.

테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다. 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.

### input

```
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
```

### output
각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.

```
1
2
5
```

### :computer: Code

```
from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    important = list(map(int, input().split()))
    queue = deque()
    result = 0

    for i in range(N):
        queue.append((i, important[i]))

    while queue:
        index, imp = queue.popleft()
        flag = True
        for idx, pri in queue:
            if pri > imp:
                flag = False
                break
        if flag:
            result += 1
            if index == M:
                print(result)
                break

        else:
            queue.append((index, imp))
```
### 📝 Solution
문제의 시간제한은 2초이다. 따라서 시간 복잡도 계산시 2억번 이하면 수행하면 된다. 먼저 큐의 특성 FIFO을 이용해야 한다. 예를들어 11911 같은 경우는 앞에 1은 다시 뒤로 들어가고 9가 뽑히고 나머지 1이 순서대로 뽑히는 구조이다. 그 특성일 이해하면 문제를 푸는데는 어려움이 없을 것이다. 큐의 첫 번째 원소를 빼서 중요도를 나머지 큐에 있는 것들과 비교한다. 비교후에 가장 큰 것이면 result에 +1을 해준다. 아니면 다시 뒤로 넣어준다. 그리고 비교후에 가장 큰 것이고 찾고 싶은 인덱스의 번호와 현재 인덱스가 같으면 출력을 해주면 된다.

### :speech_balloon: Problem
널리 잘 알려진 자료구조 중 최소 힙이 있다. 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

1. 배열에 자연수 x를 넣는다.
2. 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.

프로그램은 처음에 비어있는 배열에서 시작하게 된다.

### :warning: Limit
첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 자연수는 2<sup>31</sup>보다 작다.

### input

```
9
0
12345678
1
2
0
0
0
0
32
```
### output
입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.

```
0
1
2
12345678
0
```

### :computer: Code

```
import heapq
import sys

input = sys.stdin.readline

N = int(input())
queue = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if queue:
            print(heapq.heappop(queue))
        else:
            print(0)
    else:
        heapq.heappush(queue, x)
```

### 📝 Solution
이 문제의 시간 복잡도는 1억 이하가 나와야 풀 수 있다. 따라서 일반적인 queue로 구현하면 대부분이 다 시간초과가 뜰 것이다. 또한 최소 원소를 찾아주는 heapq를 이용해 구현하면 쉬울 것이다. 파이썬 특성상 입력 시간이 오래 걸리는 경우가 있어 그 시간을 짧게 해주는 sys.stdin.readline 라이브러리를 이용해준다.


### :speech_balloon: Problem
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

### :warning: Limit
첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.

### input

```
10 5
1 2 3 4 2 5 3 1 1 2
```

### output
첫째 줄에 경우의 수를 출력한다.

```
3
```

### :computer: Code
```
N, M = map(int, input().split())
Array = list(map(int, input().split()))

result = 0
start = [0, 0]

while start[0] < N or start[1] < N:
    if start[0] < N and start[1] < N:
        if start[0] == start[1]:
            if Array[start[0]] == M:
                result += 1
                start[1] += 1
            else:
                start[1] += 1
        else:
            if sum(Array[start[0]:start[1] + 1]) == M:
                result += 1
                start[0] += 1
            elif sum(Array[start[0]:start[1] + 1]) < M:
                start[1] += 1
            else:
                start[0] += 1

    elif start[0] == M:
        result += 1
        start[0] += 1
    else:
        start[0] += 1

print(result)
```

### 📝 Solution
이 문제는 시간제한이 0.5초이다. 따라서 시간 복잡도를 구한 계산이 5천만 이하면 수행하면 된다. 이 문제는 투 포인터를 이용한 구간합을 구하는 가장 좋은 예시이다. 투 포인터는 인덱스 2개를 가지고 결과를 구하는 것이다. 여기서 보면 start를 둘다 인덱스 0번째 부터 시작해 start[0], start[1]이 같을 때, sum이 M보다 작을 때, 클 때, 그리고 마지막으로 start[0]만 아직 끝까지 못 갔을 때 인 경우를 따져주면 풀 수 있을 것이다.

### :speech_balloon: Problem
바로 어제 최백준 조교가 방 열쇠를 주머니에 넣은 채 깜빡하고 서울로 가 버리는 황당한 상황에 직면한 조교들은, 702호에 새로운 보안 시스템을 설치하기로 하였다. 이 보안 시스템은 열쇠가 아닌 암호로 동작하게 되어 있는 시스템이다.

암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다. 또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다. 즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.

새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다. 이 알파벳을 입수한 민식, 영식 형제는 조교들의 방에 침투하기 위해 암호를 추측해 보려고 한다. C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.

### :warning: Limit
첫째 줄에 두 정수 L, C가 주어진다. (3 ≤ L ≤ C ≤ 15) 다음 줄에는 C개의 문자들이 공백으로 구분되어 주어진다. 주어지는 문자들은 알파벳 소문자이며, 중복되는 것은 없다.

### input

```
4, 6
a t c i s w
```

### output
각 줄에 하나씩, 사전식으로 가능성 있는 암호를 모두 출력한다.

```
acis
acit
aciw
acst
acsw
actw
aist
aisw
aitw
astw
cist
cisw
citw
istw
```

### :computer: Code

```
from itertools import combinations

L, C = map(int, input().split())
String = sorted(list(map(str, input().split())))
vowel = ('a', 'e', 'i', 'o', 'u')


comb = list(combinations(String, L))

for now in comb:
    count = 0
    for i in now:
        if i in vowel:
            count += 1
    if (count >= 1) and (count <= L-2):
        print(''.join(now))
```

### 📝 Solution
이 문제의 시간 제한은 2초이다. 따라서 이 문제는 시간 복잡도가 2억 이하가 되야 수행을 한다. 조합 문제의 대표적인 예시이자 구현 문제이다. 처음 들어 갈 때부터 정렬을 해서 리스트에 저장을 해준다면 조합을 할 때에도 정렬이 되어 조합을 해준다. 또한 조합이 반복 되는 조합이 나오면 안되므로 combinations을 써준다. 그 결과를 리스트로 저장을 하고 원소 하나하나를 비교해 모음의 개수를 세어준다. 여기서 최소 1개의 모음과 최소 2개의 자음이 들어가기 때문에 총 개수에서 모음을 센 변수를 빼주면 자음의 개수를 구할 수 있다. 그래서 2개 이상만 들어가면 되므로 L - 2가 들어가는 것이다.