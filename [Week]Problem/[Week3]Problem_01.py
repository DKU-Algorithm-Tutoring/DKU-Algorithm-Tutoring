n = int(input())
stack = []
seq = []
count = 0
result = True
for i in range(1, n+1):
    num = int(input())
    while count < num:
        count += 1
        stack.append(count)
        seq.append('+')
    if stack[-1] == num:
        stack.pop()
        seq.append('-')
    else:
        result = False
if result:
    print('\n'.join(seq))
else:
    print('NO')
