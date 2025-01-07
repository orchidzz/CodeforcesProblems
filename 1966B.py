def solve(r, c, matrix):
    # corners
    c1 = matrix[0][0]
    c4 = matrix[r-1][c-1]
    c2 = matrix[0][c-1]
    c3 = matrix[r-1][0]
    if c1 == c4 or c2 == c3:
        return "YES"
    # triangle
    if c1 == c2 and c!=1:
        for cell in matrix[r-1]:
            if cell == c1:
                return "YES"
    if c3 == c4 and c!= 1:
        for cell in matrix[0]:
            if cell == c3:
                return "YES"
    if c1 == c3 and r!=1:
        for i in range(rows):
            if matrix[i][c-1] == c1:
                return "YES"
    if c2 == c4 and r != 1:
        for i in range(rows):
            if matrix[i][0] == c2:
                return "YES"
    return "NO"

if __name__ == "__main__":
    for _ in range(int(input())):
        rows, cols = map(int, input().split(" "))
        matrix = []
        for idx in range(rows):
            matrix.append(str(input()))
        print(solve(rows, cols, matrix))


