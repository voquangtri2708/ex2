G,P = [],[]
n = 0

def Split(string):
    k = string.index(' ')
    str = string[0:k]
    a = int(str, base=10)
    m = string.index(' ',k+1, -1)
    str = string[k+1:m]
    b = int(str, base=10)
    str = string[m+1:len(string)]
    c = int(str, base=10)
    return a,b,c

def Init(path, G):
    f = open(path)
    string = f.readline()
    n,a,z = Split(string)


    for i in range(n+1):
        G.append([])
        for j in range(n+1):
            G[i].append(0)


    while 1:
        string = f.readline()
        if not string:
            break
        i,j,x = Split(string)
        G[i][j] = G[j][i] = x
    f.close()
    return n,a,z

def Check(M,n,u):
    for i in range(1,n+1):
        if M[i] == u:
            return True
    return False

def ViewMatrix(G,n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print('%d' % G[i][j], end=' ')
        print()

def Breadth_First_Search(G,P,n,s,g):
    Open, Close = [], []
    for j in range(n+3):
        Open.append(0)
        Close.append(0)
        P.append(0)
    front = 1
    rear = 1
    Open[rear] = 5
    P[s] = s
    while front <= rear:
        u = Open[front]
        front += 1
        if u == g:
            return 1
        for v in range(1,n+1):
            if G[u][v] != 0 and not Check(Open,n,v) and not Check(Close,n,v):
                rear += 1
                Open[rear] = v
                P[v] = u
        Close[u] = u
    return 0

def Detph_First_Search(G,P,n,s,g):
    Open, Close = [],[]
    for j in range(n+3):
        Open.append(0)
        Close.append(0)
        P.append(0)
    top = 1
    Open[top] = s
    P[s] = s
    while top > 0:
        u = Open[top]
        top -= 1
        if u == g:
            return 1
        for v in range(1,n+1):
            if G[u][v] != 0 and not Check(Open,n,v) and not Check(Close,n,v):
                top += 1
                Open[top] = v
                P[v] = u
        Close[u] = u
    return 0


def Print(P,n,s,g):
    Path = []
    for i in range(0,n+1):
        Path.append(0)
    
    print('Duong di tu %d'%s, ' den %d'%g, ' la \n', end=' ')
    Path[0] = g
    i = P[g]
    k = 1
    while i != s:
        Path[k] = i
        k += 1
        i = P[i]
    Path[k] = s
    for j in range(0,k+1):
        i = k - j
        if i > 0:
            print('%d => '%Path[i], end=' ')
        else:
            print('%d'%Path[i],end=' ')
            
'''
def Print(P, n, s, g):
    # Create an empty path list
    Path = []
    
    # If there's no path from s to g, return an error message
    if P[g] == 0:
        print("No path found from %d to %d" % (s, g))
        return
    
    print('Path from %d' % s, ' to %d' % g, ' is:\n', end=' ')
    
    # Trace back from goal to start using the P array
    while g != s:
        Path.append(g)
        g = P[g]
    Path.append(s)
    
    # Print the path in correct order (from start to goal)
    for i in range(len(Path) - 1, -1, -1):
        if i > 0:
            print('%d => ' % Path[i], end=' ')
        else:
            print('%d' % Path[i], end=' ')
    print()
'''

def main():
    print('Hello World !!')

    n,s,g = Init("graph2.inp", G)
    Detph_First_Search(G,P,n,s,g)
    Print(P,n,s,g)
    # print('Xem ma tran G : ', end='\n')
    # ViewMatrix(G,n)
    


if __name__ == "__main__":
    main()