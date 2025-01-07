def solve(li, k, n):
    remainder = [-1] * n
    for i in range(len(li)):
        remainder[i] = li[i]%k
        if remainder[i] == 0:
            remainder[i] = k
    if k == 4:
        ans = max(remainder)
        num_2 = 0
        num_1 = 0
        for i in remainder:
            if i == 2:
                num_2 += 1
            elif i == 1:
                num_1 += 1
        if num_2 >= 2:
            ans = 0
        elif num_1 >= 2 and num_2 == 0:
            ans = (k-max(ans, 2))%k
        elif num_1 >= 1 and num_2 == 1:
            ans = (k-max(ans, 3))%k
        else:
            ans = (k - max(ans, 1)) % k
    else:
        ans = (k-max(remainder))%k
    print(ans)


if __name__ == "__main__":
    for _ in range(int(input())):
        n, k = map(int, input().split(" "))
        li = list(map(int, input().split(" ")))
        solve(li, k, n)