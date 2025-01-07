if __name__ == "__main__":
    n = int(input())
    li = list(map(int, input().split(" ")))
    table = {1: 0, 2: 0}
    for i in range(n):
        if li[i] == 1:
            table[1] += 1
        else:
            table[2] += 1
    res = 0
    if table[1] >= table[2]:
        res += table[2]
        table[1] -= table[2]
        res += (table[1]//3)
    else:
        res += table[1]
        table[2] -= table[1]
    print(res)