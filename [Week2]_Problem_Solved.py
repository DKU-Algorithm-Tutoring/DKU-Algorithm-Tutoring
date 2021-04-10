import math

#1
i = 1
sum = 0
while i < 1000 :
    if i % 3 == 0 :
        sum += i
    i += 1
print(sum)

#2
i2 = 1
while i2 < 6 :
    print("*" * i2, end = '')
    print("")
    i2 += 1

#3
for i3 in range (1, 101) :
    print(i3)

#4
A = [70, 60, 55, 75, 95, 80, 80, 85, 100]
stu_up = []
stu_down = []
sum = 0
for i in range(len(A)) :
    sum += A[i]
avg = sum / len(A)
for i in range(len(A)) :
    if A[i] > avg :
        stu_up.append(A[i])
    elif A[i] < avg :
        stu_down.append(A[i])

print(stu_up)
print(stu_down)

#5
def is_odd(num1) :
    if num1 % 2 == 0 :
        return 1
    else :
        return 0

#6
String = "A:B:C:D"
String = String.split(':')
String = "#".join(String)
print(String)

#7
def fib(num1) :
    result = 0
    for i in range (num1) :
        result += num1
    return result

#8
N = int(input())
for i in range (1, 10) :
    print(N , "x" , i , "=" , i * N)

#9
def cal(num1, op, num2) :
    if op == '+' :
        return num1 + num2
    elif op == '-' :
        return num1 - num2
    elif op == '*' :
        return num1 * num2
    elif op == '/' :
        return num1 / num2
    else :
        print("잘못된 연산기호")
        return 0

#10
prime_check = [True for _ in range(101)]
for i in range(2, 10) :
    for j in range(i * 2, 101, i) :
        prime_check[j] = False
for i in range(2, 101) :
    if prime_check[i] is True :
        print(i)





















