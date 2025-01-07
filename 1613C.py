def solve(n, h, a):
    left = 0
    right = h
    k = h
    while left <= right:
        k = (left+right)>>1
        total = 0
        for i in range(n):
            if i<n-1:
                total += min(k, a[i+1] - a[i])
            else:
                total += k
        if total < h:
            left = k+1
            k = left
        else:
            right = k-1
    return k

if __name__ == "__main__":
    for _ in range(int(input())):
        n, h = map(int, input().split(" "))
        a = list(map(int, input().split(" ")))

        print(solve(n, h, a))