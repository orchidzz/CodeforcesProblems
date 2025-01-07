def solve(n, k, li):
    cow = n
    for i in range(n):
        if li[i] > li[k-1] and i != k-1:
            cow = i
            break
    if cow > k-1:
        return cow-1
    elif cow < k-1:
        # swap with cow 1
        li[0], li[k - 1] = li[k - 1], li[0]
        a = 0
        for i in range(1, n):
            if li[i] > li[0]:
                break
            else:
                a += 1
        # swap with cow i
        li[0], li[k - 1] = li[k - 1], li[0]
        li[cow], li[k-1] = li[k-1], li[cow]
        b = 1 if cow > 0 else 0
        for i in range(cow+1, n):
            if li[i] > li[cow]:
                break
            else:
                b += 1
        return max(a,b)



if __name__ == "__main__":
    for _ in range(int(input())):
        n, k = map(int, input().split(" "))
        li = list(map(int, input().split(" ")))
        print(solve(n, k, li))