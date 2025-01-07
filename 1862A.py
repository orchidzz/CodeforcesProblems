def solve(li):
    n = len(li)
    m = len(li[0])
    name = "vika"
    k = 0
    for j in range(m):
        for i in range(n):
            if li[i][j] == name[k]:
                k += 1
                break
        if k == 4:
            print("YES")
            return

    print("NO")



if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split(" "))
        li = [""]*n
        for i in range(n):
            li[i] = str(input())

        solve(li)