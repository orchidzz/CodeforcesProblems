def solve(s):
    a = 0
    b = 0
    bestA = 0
    bestB = 0
    for i in range(len(s)):
        if i&1 == 0: # even
            if s[i] == '1':
                a += 1
            elif s[i] == '?':
                bestA += 1
        else:
            if s[i] == '1':
                b += 1
            elif s[i] == '?':
                bestB += 1
        if b+bestB-a > (9-i)//2 or a+bestA-b > (10-i)//2:
            print(i+1)
            return
    print(10)


if __name__ == "__main__":
    for _ in range(int(input())):
        s = str(input())
        solve(s)