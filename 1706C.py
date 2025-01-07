def solve(n, h):
    if n&1:
        ans = 0
        for i in range(1, n-1, 2):
            ans += max(0, 1+ max(h[i-1], h[i+1])-h[i])
        return ans
    else:
        dp = [0]*n
        for i in range(1, n-1):
            if i&1:
                dp[i] = dp[i - 2]+ max(0, 1 + max(h[i - 1], h[i + 1]) - h[i])
            else:
                dp[i] = min(dp[i-2], dp[i-3]) + max(0,  1+ max(h[i-1], h[i+1])-h[i])
        return min(dp[-2], dp[-3])

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        h = list(map(int, input().split(" ")))
        print(solve(n, h))