def solve(n, l, r, a):
    num_sum = 0
    ans = 0
    left = 0
    for i in range(n):
        num_sum += a[i]
        while left <= i and num_sum > r:
            num_sum -= a[left]
            left += 1
        if l <= num_sum <= r:
            ans += 1
            num_sum = 0
            left = i+1
    print(ans)


if __name__ == "__main__":
    for _ in range(int(input())):
        n, l, r = map(int, input().split(" "))
        a = list(map(int, input().split(" ")))
        solve(n, l, r, a)