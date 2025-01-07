def solve(n, k):
    # alpha = "abcdefghijklmnopqrstuvwxyz"
    # # subsequence = alpha[:k].copy()
    res = [""] * (k*n)
    c = 0
    for i in range(len(res)):
        if c < k:
            res[i] = chr(97+c)
        else:
            c = 0
            res[i] = chr(97+c)
        c += 1
    return "".join(res)


if __name__ == "__main__":
    for _ in range(int(input())):
        n, k = map(int, input().split(" "))
        print(solve(n, k))