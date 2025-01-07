def solve(s):
    a = 0
    b = 0
    for i in range(len(s)):
        a += (s[i - 1] == '0' and s[i] == '1')
        b += (s[i - 1] == '1' and s[i] == '0')
    return a - (a > 0) + b + 1



if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        print(solve(s))