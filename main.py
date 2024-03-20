"""
Name: 2x2 Matrix Multiplication
Description: multiplies two matrixes, another school related script
"""

matrix1 = []
matrix2 = []

i = 0
for row in range(2):
    for column in range(2):
        matrix1.append(int(input(f"a-{row}{column}: ")))


for row in range(2):
    for column in range(2):
        matrix2.append(int(input(f"b-{row}{column}: ")))
                         
print(f"[{(matrix1[0] * matrix2[0]) + (matrix1[1] * matrix2[2])} {(matrix1[0] * matrix2[1]) + (matrix1[1] * matrix2[3])}]")

print(f"[{(matrix1[2] * matrix2[0]) + (matrix1[3] * matrix2[2])} {(matrix1[2] * matrix2[1]) + (matrix1[3] * matrix2[3])}]")