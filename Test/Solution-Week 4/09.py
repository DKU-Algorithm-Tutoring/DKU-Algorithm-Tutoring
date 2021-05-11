"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com
title : 럭키 스트레이트
게임의 아웃복서 캐릭터는 필살기인 '럭키 스트레이트' 기술이 있습니다. 이 기술은 매우 강력한 대신에 게임 내에서 점수가 특정 조건을 만족할 때만 사용할 수 있습니다.
특정 조건이란 현재 캐릭터의 점수를 N이라고 할 때 자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이
동일한 상황을 의미합니다. 예를 들어 현재 점수가 123,402라면 왼쪽 부분의 각 자릿수의 합은 1 + 2 + 3, 오른쪽 부분의 각 자릿수의 합은 4 + 0 + 2 이므로
두 합이 6으로 동일하여 럭키 스트레이트를 사용할 수 있습니다.
현재 점수 N이 주어지면 럭키 스트레이트를 사용할 수 있는 상티인지 아닌지를 알려주는 프로그램을 작성하세요.
description : 구현
"""

N = input()
half_length = len(N) // 2
result1 = 0
result2 = 0
for i in range(len(N)):
    if i < half_length:
        result1 += int(N[i])
    else:
        result2 += int(N[i])

if result1 == result2:
    print('LUCKY')
else:
    print('READY')