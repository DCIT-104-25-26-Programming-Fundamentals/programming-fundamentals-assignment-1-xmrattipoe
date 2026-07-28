def read_matrix(rows, cols, label):
    print(f"Enter {label}:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(val) for val in row))


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(a, b):
    rows = len(a)
    cols = len(a[0])
    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]

    return result


def multiply_matrices(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])
    result = [[0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            result[i][j] = total

    return result


if __name__ == "__main__":
    print("--- Part A: Transpose ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix_a = read_matrix(rows, cols, "matrix")
    print("Transposed Matrix:")
    print_matrix(transpose(matrix_a))

    print("\n--- Part B: Add Two Matrices ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    m1 = read_matrix(rows, cols, "first matrix")
    m2 = read_matrix(rows, cols, "second matrix")
    print("Sum Matrix:")
    print_matrix(add_matrices(m1, m2))

    print("\n--- Part C: Multiply Two Matrices ---")
    rows_a = int(input("Enter rows for matrix A: "))
    cols_a = int(input("Enter columns for matrix A (= rows for matrix B): "))
    cols_b = int(input("Enter columns for matrix B: "))
    ma = read_matrix(rows_a, cols_a, "matrix A")
    mb = read_matrix(cols_a, cols_b, "matrix B")
    print("Product Matrix:")
    print_matrix(multiply_matrices(ma, mb))

