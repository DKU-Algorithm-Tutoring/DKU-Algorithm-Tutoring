"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com
title : 모험가 길드
한 마을에 모험가가 N명 있습니다. 모험가 길드에서는 N명의 모험가를 대상으로 '공포도'를 측정했는데,
'공포도'가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어집니다.
모험가 길드장인 동빈이는 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로
구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했습니다.
동빈이는 최대 몇개의 모험가 그룹을 만들 수 있는지 궁금합니다.
동빈이를 위해 N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하세요.
description : 그리디 알고리즘
"""

import sys

N = int(sys.stdin.readline().rstrip())
X = list(map(int, sys.stdin.readline().rstrip().split()))

total = 0
X.sort()

for i in set(X):
    if X.count(i) >= i:
        total += 1
print(total)