def solve(x):
    arr = []
    for i in range(31):
        mask = 1<<i
        num = (x & mask)>>i
        arr.append(str(num))
    print(len(arr))
    rem = False
    for i in range(1, 31):
        if rem and arr[i] == "1":
            arr[i] = "0"
            continue
        elif rem and arr[i] == "0":
            arr[i] = "1"
            rem = False
            continue
        if arr[i] != "0" and arr[i-1] != "0":
            arr[i] = "0"
            arr[i-1] = "-1"
            if arr[i+1] == "1":
                rem = True
            else:
                arr[i+1] = "1"
    print(" ".join(arr))

if __name__ == "__main__":
    for _ in range(int(input())):
        x = int(input())
        solve(x)