import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0 for _ in range(N)]
for _ in range(M):
    i, j, k = map(int, input().split())
    for index in range(i-1, j):
        arr[index] = k
    
print(*arr)