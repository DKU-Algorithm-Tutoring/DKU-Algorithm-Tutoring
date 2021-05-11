"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 시각
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.
예를들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시간이다.
"""

N = int(input())

count = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

"""
N = int(input())
count = 0
time = [0, 0, 0]
for i in range(N + 1):
    time[1] = 0
    if '3' in str(time[0]):
        count += (60 * 60)
        time[0] += 1
    else:
        for j in range(61):
            time[2] = 0
            if '3' in str(time[1]):
                count += 60
                time[1] += 1
            else:
                if j == 59:
                    time[0] += 1
                else:
                    for k in range(60):
                        if '3' in str(time[2]):
                            count += 1
                            time[2] += 1
                        else:
                            time[2] += 1
                            if k == 59:
                                time[1] += 1
print(count)
"""