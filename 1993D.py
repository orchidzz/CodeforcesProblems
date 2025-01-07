def solve(n, s):
    s.sort()
    if s[0] % s[1] != 0:
        print("YES")
        return
    elif n>2:
        for i in range(2, n):
            if s[i] % s[0] != 0:
                print("YES")
                return
    print("NO")


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        s = list(map(int, input().split(" ")))

        solve(n, s)
