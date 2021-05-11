"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com
title : 문자열 재정렬
알파벳 대문자와 숫자 (0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를
더한 을 이어서 출력합니다. 예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.
description : 구현
"""

S = input()
String = []
result = 0

for i in S:
    if 48 <= ord(i) <= 57:
        result += int(i)
    else:
        String.append(i)
String.sort()
String.append(result)
[print(x, end='') for x in String]