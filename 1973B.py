def solve(n, a):
    left = 1
    right = n
    ans = 1
    while left <= right:
        mid = (left+right)>>1
        lonely = True
        bits = [0] * 20
        for i in range(mid):
            for j in range(20):
                if a[i]&(1<<j):
                    bits[j] += 1
        pt1 = mid
        while pt1 < n:
            start = a[pt1-mid]
            for j in range(20):
                if start&(1<<j):
                    if bits[j]-1 == 0 and a[pt1]&(1<<j) == 0:
                        lonely = False
                        pt1 = n
                        break
                if a[pt1]&(1<<j) and bits[j] == 0:
                    lonely = False
                    pt1 = n
                    break
                if a[pt1]&(1<<j):
                    bits[j]+= 1
                if start&(1<<j):
                    bits[j] -= 1
            pt1 += 1
        if not lonely:
            left = mid+1
        else:
            ans = mid
            right = mid-1
    return ans

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split(" ")))
        print(solve(n, a))