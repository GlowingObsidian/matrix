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
    if(len(matrix)==1 and len(matrix[0])==1):
        det=matrix[0][0]
    else:
        sign=1
        for i in range(0,len(matrix[0])):
            sub_matrix=list()
            for j in range(1,len(matrix)):
                temp=list()
                for k in range(0,len(matrix[j])):
                    if(k==i):
                        None
                    else:
                        temp.append(matrix[j][k])
                sub_matrix.append(temp)
            det=det+(sign*matrix[0][i]*determinant(sub_matrix))
            sign=sign*-1
    return det

def transpose(matrix):
    trns_matrix=list()
    for i in range(0,len(matrix[0])):
        temp=list()
        for j in range(0,len(matrix)):
            temp.append(matrix[j][i])
        trns_matrix.append(temp)
    return trns_matrix

def adjoint(matrix):
    adj_matrix=list()
    if(len(matrix)==1 and len(matrix[0])==1):
        adj_matrix=list(map(list,matrix))
    else:
        pre_adj_matrix=null(len(matrix),len(matrix[0]))
        sign=-1
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                sub_matrix=list()
                for k in range(0,len(matrix)):
                    temp=list()
                    for l in range(0,len(matrix[k])):
                        if(k!=i and l!=j):
                            temp.append(matrix[k][l])
                    if(len(temp)!=0):
                        sub_matrix.append(temp)
                pre_adj_matrix[i][j]=(sign**(i+j))*determinant(sub_matrix)
        adj_matrix=transpose(pre_adj_matrix)
    return(adj_matrix)

