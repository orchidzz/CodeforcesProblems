def solve(n, li):
    moves = set()
    for i in range(n):
        x = li[i][0]
        y = li[i][1]
        if x > 0:
            moves.add("R")
        elif x < 0:
            moves.add("L")
        if y > 0:
            moves.add("U")
        elif y < 0:
            moves.add("D")

    if len(moves) <= 3:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        li = [[]] * n
        for pt in range(n):
            li[pt] = list(map(int, input().split(" ")))

        solve(n, li)
