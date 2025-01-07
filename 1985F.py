def solve(h,n,a,c):
    ans = 0
    left = 0
    right = h<<18
    while left <= right:
        mid = (left+right)>>1
        damage = 0
        for i in range(n):
            damage += (((mid-1)//c[i]+1) * a[i])
            if damage >= h:
                break
        if damage >= h:
            ans = mid
            right = mid-1
        else:
            left = mid+1
    return ans


if __name__ == "__main__":
    for _ in range(int(input())):
        h, n = map(int, input().split(" "))
        a = list(map(int, input().split(" ")))
        c = list(map(int, input().split(" ")))
        print(solve(h,n,a,c))