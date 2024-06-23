'''
# def Inputdata():
#     a = float(input('Nhap a = '))
#     b = float(input('Nhap b = '))
#     c = float(input('Nhap c = '))
#     return a,b,c

# def Max3(a,b,c):
#     max = a
#     if b > a:
#         max = b
#     if c > b:
#         max = c
    
#     return max
'''

def GT(n):
    if n <= 2:
        return n
    else:
        return n * GT(n-1)
    
def TongLe(M):
    tongle = 0
    for i in M:
        tongle += (i%2 == 1)*i
    return tongle

def CreateArr(M,n):
    for i in range(n):
        M.append(int(input('Nhap vao so thu %d : ' %(i+1))))

def InputN(x):
    try:
        n = int(input('Nhap '+x))
        if n <= 0:
            exit()
        return n
    except:
        print('Phai nhap so tu nhien !!')
        exit()



def createMatrix(A,m,n):
    for i in range(m):
        A.append([])
        for j in range(n):
            x = int(InputN(''))
            A[i].append(x)

def sumMatrix(A,B,m,n):
    C = []
    for i in range(m):
        C.append([])
        for j in range(n):
            C[i].append(A[i][j] + B[i][j])
    return C

def MulMatrix(A,B,m,n):
    C = []
    for i in range(m):
        C.append([])
        for j in range(n):
            x = 0 
            for k in range(m):
                x += A[i][k]*B[k][j]
            C[i].append(x)
    return C



def main():
    A,B = [],[]
    m = InputN('dong : ')
    n = InputN('cot  : ')
    # n = InputN()
    # CreateArr(M,n)
    # print(M)
    # print('Tong mang la : ', sum(M))
    # print('Tong le la   : ', TongLe(M))

    # print('Mang khi duoc sap xep la \n', M.sort())

    # k = int(input("Nhap so can xoa k = "))
    # M.remove(k)
    # print(M)

    # m = int(input("Nhap so can them m = "))
    # index = InputN()
    # M.insert(index,m)
    # print(M)

    createMatrix(A,m,n)
    createMatrix(B,m,n)
    print(sumMatrix(A,B,m,n))
    
    

if __name__ == "__main__":
    main()