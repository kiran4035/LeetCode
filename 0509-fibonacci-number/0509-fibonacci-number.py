class Solution:
    def fib(self, n: int) -> int:
        def fib(n):
            if dp[n] != -1:
                return dp[n]
            dp[n] =  fib(n-1) + fib(n-2)
            return dp[n]

        if n == 0:
            return 0
        if n ==1: return 1
        dp = [-1 for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        return fib(n)
