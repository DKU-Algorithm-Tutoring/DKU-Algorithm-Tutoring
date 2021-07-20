## :star: 3주차 수업

### 주요 자료구조

#### stack
![image](https://user-images.githubusercontent.com/78870076/113569287-332a7200-964d-11eb-881f-260d871d0528.png)

#### queue

![image](https://user-images.githubusercontent.com/78870076/113569353-535a3100-964d-11eb-89ef-5af279eff976.png)

#### 시간복잡도 및 공간복잡도
- 시간 복잡도 : 알고리즘 수행 시간
- 공간 복잡도 : 알고리즘의 메모리 사용량

보통 코딩 테스트에서는 시간 복잡도는 1억, 공간복잡도는 데이터의 개수가 1,000만 단위를 넘지 않게 알고리즘을 설계 해야한다.                                                      
### 주요라이브러리의 문법과 유의점
**표준 라이브러리**란 특정한 프로그래밍 언어에서 자주 사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리를 의미한다. 파이썬에서 지원하는 표준 라이브러리는 굉장히 다양하지만, 코딩 테스트를 준비하며 반드시 알아야 하는 라이브러리는 6가지 정도이다.

- 내장함수 : print(), input()과 같은 기본 입출력 기능부터 sorted()와 같은 정렬 기능을 포함하고 있는 기본 내장 라이브러리이다.
- itertools : 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리이다. 순열과 조합 라이브러리를 제공한다.
- heapq : 힙(Heap) 기능을 제공하는 라이브러리이다. 우선순위 큐 기능을 구현하기 위해 사용한다.
- bisect : 이진 탐색(Binary Search) 기능을 제공하는 라이브러리이다.
- collections : 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함하고 있는 라이브러리이다.

#### 내장함수
- input()
- print()
- min() : 피라미터가 2개 이상 들어왔을 때 가장 작은 값을 반환한다.
- max() : 피라미터가 2개 이상 들어왔을 때 가장 큰 값을 반환한다.
- eval() : 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환한다.

```
result = eval('(3 + 5) * 7')
print(result)
```

```
56
```

#### itertools
itertools는 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리이다. 제공하는 클래스는 매우 다양하지만 코딩 테스트에서 가장 유용하게 사용할 수 있는 클래스는 **permutations, combinations**이다.

```
from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutation(data, 3))

print(result)
```

```
[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
```

combinations의 경우는 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우를 계산한다.

```
from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 2))

print(result)
```

```
[('A', 'B'), ('A', 'C'), ('B', 'C')]
```

#### heapq
파이썬에서는 힙 기능을 위해 heapq 라이브러리를 제공한다. heapq는 우선순위 큐 기능을 구현하고자 할 때 사용된다.

#### bisect
파이썬에서는 이진 탐색을 쉽게 구현할 수 있도록 bisect 라이브러리를 제공한다. bisect 라이브러리는 **정렬된 배열**에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용된다.
- bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 매소드이다.
- bisect_right(a, x) : 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 매소드이다.


#### collections
collections에서 자주 사용되는 클래스는 **deque와 Counter** 2가지이다.

```
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))
```

```
deque([1, 2, 3, 4, 5])
[1, 2, 3, 4, 5]
```

```
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(Counter['blue'])
print(Counter['green'])
print(dict(counter))
```

```
3
1
{'red' : 2, 'blue' : 3, 'green' : 1}
```

### 기타 주요 알고리즘

#### 소수의 판별(에라토스테네스의 체)
- 2부터 N까지의 모든 자연수를 나열한다
- 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
- 남은 수 중에서 i의 배수를 모두 제거한다.(i는 제거하지 않는다.)
- 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복한다.

#### 투포인터
투포인터 알고리즘은 **리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리**하는 알고리즘을 의미한다.