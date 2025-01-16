def fibo(n):
    dp = [0] * (n+3)
    dp[0] = 0; dp[1] = 1; dp[2] = 1; dp[3] = 1
    
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-3]
        
    return dp[n]


n = int(input())
print(fibo(n))