import matrix

#Draw a Matrix: matrix.draw(matrix)
#Fill a Matrix: matrix.fill(matrix)
#Null Matrix  : matrix.null(row,column)

#Addition of Matrices
#matrix.add(matrix A, matrix B)
matrix.draw(matrix.add(matrix.fill(matrix.null(int(input('Number of Rows: ')),int(input('Number of Columns: ')))),matrix.fill(matrix.null(int(input('Number of Rows: ')),int(input('Number of Columns: '))))))

#Subtraction of Matrices
#matrix.sub(matrix A, matrix B)
matrix.draw(matrix.sub(matrix.fill(matrix.null(int(input('Number of Rows: ')),int(input('Number of Columns: ')))),matrix.fill(matrix.null(int(input('Number of Rows: ')),int(input('Number of Columns: '))))))

#Scalar Multiplication
#matrix.scalar(scalar,matrix)
matrix.draw(matrix.scalar(int(input('Enter the scalar: ')),matrix.fill(matrix.null(int(input('Number of Rows: ')),int(input('Number of Columns: '))))))

#Dot product of two Matrices
#matrix.dot(matrix A, matrix B)
matrix.draw(matrix.dot(matrix.fill(matrix.null(int(input('Number of Rows: ')),int(input('Number of Columns: ')))),matrix.fill(matrix.null(int(input('Number of Rows: ')),int(input('Number of Columns: '))))))

#Determinant Calculation of a Matrix
#matrix.determinant(matrix)
print(matrix.determinant(matrix.fill(matrix.null(int(input('Number of Rows: ')),int(input('Number of Columns: '))))))

#Adjoint of a Matrix
#matrix.adjoint(matrix)
matrix.draw(matrix.adjoint(matrix.fill(matrix.null(int(input('Number of Rows: ')),int(input('Number of Columns: '))))))