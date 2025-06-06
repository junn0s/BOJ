# 11055 가장 큰 증가하는 부분 수열

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
for i in range(n):
    dp[i] = arr[i]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            # dp[i] = max(dp[i], dp[j] + arr[i])
            # 같은 의미임 (GPT)
            tmp = dp[j] + arr[i]
            if tmp > dp[i]:
                dp[i] = tmp

print(max(dp))

# 1, 101, 3, 53, 113, 6, 11, 17, 24, 32
# print(max(dp)) == 113