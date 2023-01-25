R = int(input("Enter the number of rows: "))
C = int(input("Enter the number of columns: "))
matrix = []

for i in range(R):
    a = []
    for j in range(C):
        a.append("#")
        a.append("*")
    matrix.append(a)

for i in range(R):
    for j in range(C):
        print(matrix[i][j], end="")
    print()
