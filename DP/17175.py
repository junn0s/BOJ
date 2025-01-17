def fibo(n):
    if n == 0:
        return 1
    dp = [0] * (n+1)
    dp[0] = 1; dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2] + 1) % 1000000007
        
    return dp[n]

n = int(input())
print(fibo(n))