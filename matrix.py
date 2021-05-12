def null(r,c):
    matrix=list()
    for i in range(0,r):
        temp=list()
        for j in range(0,c):
            temp.append(0)
        matrix.append(temp)
    return matrix

def fill(matrix):
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            value=int(input('Value for position '+str(i+1)+str(j+1)+': '))
            matrix[i][j]=value
    print()
    return matrix

def draw(matrix):
    for i in range(0,len(matrix)):
        print('[',end=' ')
        for j in range(0,len(matrix[i])):
            print(matrix[i][j],end=' ')
        print(']')

def add(A,B):
    if(len(A)==len(B) and len(A[0])==len(B[0])):
        C=null(len(A),len(A[0]))

    for i in range(0,len(C)):
        for j in range(0,len(C[i])):
            C[i][j] = A[i][j] + B[i][j]
    return C

def sub(A,B):
    if(len(A)==len(B) and len(A[0])==len(B[0])):
        C=null(len(A),len(A[0]))

    for i in range(0,len(C)):
        for j in range(0,len(C[i])):
            C[i][j] = A[i][j] - B[i][j]
    return C

def scalar(n,A):
    C=null(len(A),len(A[0]))
    for i in range(0,len(A)):
        for j in range(0,len(A[i])):
            C[i][j]=n*A[i][j]
    return C

def dot(A,B):
    if(len(A[1])==len(B)):
        C=null(len(A),len(B[0]))
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    C[i][j] += A[i][k] * B[k][j]
    return C

def determinant(matrix):
    det=0
    if(len(matrix)>2 and len(matrix[0])>2):
        sign=1
        for i in range(0,len(matrix[0])):
            sub_determinant=list()
            for j in range(1,len(matrix)):
                temp=list()
                for k in range(0,len(matrix[j])):
                    if(k==i):
                        None
                    else:
                        temp.append(matrix[j][k])
                sub_determinant.append(temp)
            det=det+(sign*matrix[0][i]*determinant(sub_determinant))
            sign=sign*-1             
    else:
        det=(matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
    return det

def adjoint(matrix):
    adj_matrix=list()
    for i in range(0,len(matrix[0])):
        temp=list()
        for j in range(0,len(matrix)):
            temp.append(matrix[j][i])
        adj_matrix.append(temp)
    return adj_matrix
