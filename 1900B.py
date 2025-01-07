def solve(a,b,c):
    res1 = 1 if not (c + b) & 1 else 0
    res2 = 1 if not (a + c) & 1 else 0
    res3 = 1 if not (a + b) & 1 else 0
    print(res1, res2, res3)

if __name__ == "__main__":
    for _ in range(int(input())):
        a, b, c = map(int, input().split(" "))
        solve(a,b,c)