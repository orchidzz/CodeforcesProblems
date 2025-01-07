def solve(n, s):
    res = 0
    distinct = set()
    for i in range(n):
        distinct.add(s[i])
        res += len(distinct)
    print(res)


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        s = str(input())

        solve(n, s)
