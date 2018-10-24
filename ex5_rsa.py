import math

def check(a,b):
    for i in range(3,b,2):
        if a%i ==0 and b%i ==0:
            return True
    return False

def encrypt(p,e,n):
    x = 0
    c = 1
    while x!=e:
        c = c * p
        x += 1
    print c
    return c

def keygen():
    p=int(raw_input("Enter first prime numbers"))
    q=int(raw_input("Enter second prime numbers"))

    n = p*q
    phi = (p-1)*(q-1)

    x = True
    while x:
        e = int(raw_input("enter e value between 1 and "+str(phi)))
        x = check(e,phi)
    x =True
    d=1

    while x:
        s = (d*e)%phi
        d += 1
        if s==1:
            x=False
    d -= 1
    print(n,phi,e,d)
    c=encrypt(10,e,n)
    p=encrypt(c,d,n)
    #print("public key =\{"++"\}")
keygen()
