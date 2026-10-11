# Program Involving Overloading
# Course: Python for Data Science | Loyola College, Chennai
# Student: Joe Rakesh A | Department No.: 26-PDS-002

# Exercise 09 — Program Involving Overloading
class Matrix:
    def __init__(self, data):
        if not data or not data[0]:
            raise ValueError("Matrix must not be empty")
        width = len(data[0])
        if any(len(row) != width for row in data):
            raise ValueError("All matrix rows must have the same length")
        self.data = [list(row) for row in data]
        self.rows = len(data)
        self.cols = width

    def __add__(self, other):
        if (self.rows, self.cols) != (other.rows, other.cols):
            raise ValueError("Matrix dimensions must match for addition")
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Incompatible dimensions for matrix multiplication")
        result = [
            [sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
             for j in range(other.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __repr__(self):
        return "\n".join(str(row) for row in self.data)

A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])
print("Matrix A:\n", A, sep="")
print("\nMatrix B:\n", B, sep="")
print("\nA + B =\n", A + B, sep="")
print("\nA * B =\n", A * B, sep="")
