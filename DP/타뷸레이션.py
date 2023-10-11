def fibonacci(n):
    # 테이블 초기화
    dp = [0] * (n + 1)
    
    # 초기 값 설정
    dp[0] = 0
    if n > 0:
        dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

N = int(input())
print(fibonacci(N))
