import math

def dh(a,b):
    p = 23
    g = 9

    x = (g ** a)%p
    y = (g ** b)%p

    Sa = (y ** a) % p
    Sb = (x ** b) % p

    print "SHARED KEY A="+str(Sa)+" & B="+str(Sb)
    if Sa == Sb:
        print "SUCCESS"
    else:
        print "FAILED"

dh(4,3)
