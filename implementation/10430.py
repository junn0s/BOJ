#나머지 - 구현


import sys
input = sys.stdin.readline

A, B, C = map(int, input().rstrip().split())

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)