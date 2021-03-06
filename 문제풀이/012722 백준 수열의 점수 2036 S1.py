# 왜 틀렸었지?
# 음수를 양수로 만들어서 저장하니까 된다.
# 1은 곱하면 손해
# 그 외의 경우는 곱해야 이득
# 0은 음수를 하나 지울 수 있으니 존재 여부를 기록한다.

import sys
input = sys.stdin.readline

ans = 0
pos = list()
neg = list()
zero = False
N = int(input())

for _ in range(N):
    temp = int(input())
    if temp < 0:
        neg.append(-1*temp)
    elif temp > 1:
        pos.append(temp)
    elif temp == 1:
        ans += 1
    else:
        zero = True

neg.sort(reverse=True)
pos.sort()

if len(neg)%2:
    if zero:
        neg.pop()
    else:
        ans -= neg.pop()
for i in range(len(neg)//2):
    ans += neg.pop() * neg.pop()
for i in range(len(pos)//2):
    ans += pos.pop() * pos.pop()

if pos:
    ans += pos.pop()
print(ans)