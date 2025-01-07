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
    win_ave = w // n
    loss_ave = l // n
    if win_ave == 0 and w > 0:
        win_ave += 1
    if loss_ave == 0 and l > 0:
        loss_ave += 1
    for i in range(n):
        if w >= win_ave:
            wins[i] += win_ave
            w -= win_ave
        else:
            wins[i] += w
    for i in range(n-1,-1,-1):
        if win_ave != loss_ave:
            if l >= loss_ave:
                if i == 0:
                    losses[i] += l
                    l -= l
                else:
                    losses[i] += loss_ave
                    l -= loss_ave
            else:
                losses[i] += l
                l -= l
        else:
            if l > loss_ave+1:
                losses[i] += loss_ave + 1
                l -= (loss_ave+1)
            else:
                losses[i] += l
                l -= l
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

