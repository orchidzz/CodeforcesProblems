if __name__ == "__main__":
    n, m = map(int, input().split(" "))
    li = list(map(int, input().split(" ")))
    dp = [[0]*n for _ in range(2)]

    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + max(li[i-1] - li[i], 0)
        dp[1][n-i-1] = dp[1][n-i] + max(li[n-i]-li[n-i-1], 0)

    for i in range(m):
        s, t = map(int, input().split(" "))
        if s < t:
            print(dp[0][t-1]-dp[0][s-1])
        else:
            print(dp[1][t-1]-dp[1][s-1])