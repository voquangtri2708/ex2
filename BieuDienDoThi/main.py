G =[]
P =[]
n =0

def Split(string):
    a, b, c = map(int, string.split())
    return a, b, c

def Init(path):
    G = []
    f = open(path)
    n, a, z = map(int, f.readline().split())
    for _ in range(n+1):
        G.append([0]*(n+1))
    for line in f:
        i, j, x = Split(line)
        G[i][j] = G[j][i] = x
    f.close()
    return n, a, z, G

def Check(M, n, u):
    return u in M[:n+1]

def ViewMatrix(G, n):
    for i in range(1, n+1):
        print(' '.join(map(str, G[i][1:n+1])))

# Tim duong di theo chieu rong
def Breadth_First_Search(G, P, n, s, g):
    Open = [0]*(n+3)
    Close = [0]*(n+3)
    front = 1
    rear = 1
    Open[rear] = s
    P[s] = s
    while front <= rear:
        u = Open[front]
        front = front + 1
        if u == g:
            return 1
        for v in range(1, n+1):
            if G[u][v] != 0 and not Check(Open, n, v) and not Check(Close, n, v):
                rear = rear + 1
                Open[rear] = v
                P[v] = u
                Close[u] = u
    return 0



def Print(P, n, s, g):
    Path = [0]*(n+1)
    print("\nDuong di tu %d" % s, "den %d" % g, "la\n", end=' ')
    Path[0] = g
    i = P[g]
    k = 1
    while i != s:
        Path[k] = i
        k = k + 1
        i = P[i]
    Path[k] = s
    for j in range(k, -1, -1):
        if j > 0:
            print("%d =>" % Path[j], end=' ')
        else:
            print("%d" % Path[j], end=' ')

def main():
    n, s, g, G = Init("graph2.inp")
    P = [0]*(n+3)
    Breadth_First_Search(G, P, n, s, g)
    Print(P, n, s, g)

if __name__ == "__main__":
    main()