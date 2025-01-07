def solve(n, w, l):
    if n == 1:
        if w == l:
            print(1)
        else:
            print(0)
        print(f"{w}:{l}")
        return
    wins = [0] * n
    losses = [0] * n
    match = 0
    while match < n and w > 0:
        w -= 1
        wins[match] = 1
        match += 1
    if w > 0:
        wins[0] += w
    if l > 0:
        if match == n:
            wins[0] += 1
            wins[n-1] -= 1
            losses[n-1] = l
        else:
            while match < n and l > 0:
                l -= 1
                losses[match] += 1
                match += 1
            if l > 0:
                losses[n-1] += l
    draws = 0
    for i in range(n):
        if wins[i] == losses[i]:
            draws += 1
    print(draws)
    for i in range(n):
        print(f"{wins[i]}:{losses[i]}")


if __name__ == "__main__":
    n = int(input())
    w = int(input())
    l = int(input())
    solve(n, w, l)

