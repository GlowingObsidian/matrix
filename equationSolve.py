#Using matrices to solve simultaneous linear equations in more than one variable

import matrix #importing the matrix library

#equation 1: x+y+z= 6
#equation 2: 2y+5z= -4
#equation 3: 2x+5y-z= 27

A=[[1,1,1],[0,2,5],[2,5,-1]] #3x3 matrix to hold the coefficients of each equation
B=[[6],[-4],[27]] #3x1 matrix to hold the constants of each equations

#finding the inverse of matrix A
#X=A^(-1)*B

determinant_A=matrix.determinant(A)
adjoint_A=matrix.adjoint(A)

#Mutiplying the inverse of A to B to get the value for each variable
C=matrix.scalar((1/determinant_A),matrix.dot(adjoint_A,B))

matrix.draw(C) #show the output

#x=5
#y=3
#z=-2