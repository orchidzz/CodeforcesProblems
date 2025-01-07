def solve(n, s):
    ans = 0
    for i in range(1,n):
        if s[i] == '@':
            ans += 1
        elif s[i] == s[i-1] and s[i] == '*':
            break

    print(ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        s = str(input())
        solve(n, s)