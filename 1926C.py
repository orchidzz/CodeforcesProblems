if __name__ == "__main__":
    # precompute
    dp = [0] * 200001
    for i in range(1, len(dp)):
        num = i
        s = 0
        # sum of digits
        while num:
            s = s + num % 10
            num = num // 10
        dp[i] = dp[i-1] + s
    for i in range(int(input())):
        n = int(input())
        print(dp[n])
