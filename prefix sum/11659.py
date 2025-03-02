import sys
input = sys.stdin.readline


n, m = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
sum_arr = [0] * (n+1)
sum_arr[0] = 0
sum_arr[1] = arr[0]

for i in range(1, n):
    sum_arr[i+1] = sum_arr[i] + arr[i]
    
for _ in range(m):
    i, j = map(int, input().rstrip().split())
    print(sum_arr[j] - sum_arr[i-1])