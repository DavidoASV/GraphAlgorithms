def nth_fib_rec(n):
    if n <= 1:
        return n
    return nth_fib_rec(n - 1) + nth_fib_rec(n - 2)

n = 5
result = nth_fib_rec(n)
print('nth_fib_rec:',result)

def nth_fibonacci_util(n, memo):
    if n <= 1:
        return n
    if memo[n] != -1:
        return memo[n]
    memo[n] = nth_fibonacci_util(n - 1, memo) + nth_fibonacci_util(n - 2, memo)
    return memo[n]

def nth_fib_DP(n):
    memo = [-1] * (n + 1)
    return nth_fibonacci_util(n, memo)

n = 5
result = nth_fib_DP(n)
print('nth_fib_DP:',result)

def nth_fib_DPt(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

n = 5
result = nth_fib_DPt(n)
print('nth_fib_DPt:',result)