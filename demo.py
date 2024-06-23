'''
print('Hello World')
# input()


a = int(input('Nhap a : '))
b = int(input('Nhap b : '))
c = a + b

print('a + b = ', c)
'''

import math

def Inputdata():
    print('Giai phuong trinh bac 2')
    a = float(input('Nhap a = '))
    b = float(input('Nhap b = '))
    c = float(input('Nhap c = '))
    return a,b,c

def SolveEqual(a,b,c):
    if a == 0 and b == 0 and c == 0:
        print('Phuoong trinh vo so nghiem !')
    elif a == 0 and b == 0 and c != 0:
        print('Phuong trinh vo nghiem')
    elif a == 0 and b != 0:
        x = -c/b
        print('Phuong trinh bac 1 x = ', x)
    else:
        delta = math.pow(b,2) - 4*a*c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            print('Phuong trinh co 2 nghiem phan biet \n')
            print('x1 = %.3lf'%x1, '\nx2 = %.3lf'%x2)
        elif delta == 0:
            x0 = -b/(2*a)
            print('Phuong trinh co nghiem kep x = %.3lf'%x0)
        else:
            print('Phuong trinh vo nghiem thuc')

def main():
    a,b,c = Inputdata()
    SolveEqual(a,b,c)

if __name__ == "__main__":
    main()