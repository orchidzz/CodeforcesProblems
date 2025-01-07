def solve(n, k, m, s):
    flags = set()
    count = 0
    c = ""
    for i in range(m):
        flags.add(s[i])
        if len(flags) == k:
            c += s[i]
            count+=1
            if count == n:
                print("YES")
                return
            flags.clear()
    print("NO")
    char = ''
    for i in range(k):
        if not chr(i+97) in flags:
            char = chr(i+97)
            break
    print(c + char*(n-len(c)))


if __name__ == "__main__":
    for _ in range(int(input())):
        n, k, m = map(int, input().split(" "))
        s = input()
        solve(n, k, m, s)