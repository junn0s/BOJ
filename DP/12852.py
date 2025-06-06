def makeOne(n):
    dp = [0] * (n + 1)
    path = [0] * (n + 1) 
    dp[1] = 0 

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        path[i] = i - 1

        if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1
            path[i] = i // 2

        if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
            dp[i] = dp[i // 3] + 1
            path[i] = i // 3

    result_path = []
    while n > 0:
        result_path.append(n)
        n = path[n]


    return result_path


n = int(input())
res = makeOne(n)
print(len(res)-1)
for num in res:
    print(num, end=' ')
