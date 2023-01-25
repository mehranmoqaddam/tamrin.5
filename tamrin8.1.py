def shatranj():

    R = int(input("Enter the number of rows: "))
    C = int(input("Enter the number of columns: "))
    matrix = []

    for i in range(R):
        a = []
        b = []
        for j in range(C):
            a.append("#")
            b.append("*")
            b.append("#")
            a.append("*")
        matrix.append(a)
        matrix.append(b)
    for i in range(R):
        for j in range(C):
            print(matrix[i][j], end="",)
        print()
shatranj()