def solve(n, li):
    li.sort()
    for a in range(n-2):
        b = a+1
        c = b + 1
        if li[a]+li[b] > li[c] and li[a]+li[c] > li[b] and li[c]+li[b] > li[a]:
            print("YES")
            return
    print("NO")

if __name__ == "__main__":
    n = int(input())
    li = list(map(int, input().split(" ")))
    solve(n, li)