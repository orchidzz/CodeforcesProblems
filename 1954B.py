def solve(n, li):
    ans = 300000  # highest num to remove for longest test case
    count = 0
    for i in range(n):
        if li[i] != li[0]:
            ans = min(ans, count)
            count = 0
        else:
            count += 1
    ans = min(ans,count) if count != n else -1
    return ans

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        li = list(map(int, input().split(" ")))
        print(solve(n, li))