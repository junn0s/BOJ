# 약수 구하기

n, k = map(int, input().split())
arr = []
for i in range(1, n+1):
    if n % i == 0:
        arr.append(i)

num = len(arr)
if k > num:
    print(0)
else:
    print(arr[k-1])
