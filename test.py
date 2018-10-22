def fence(text,n):
    fence = [[None]*len(text) for i in range(n)]
    rail = range(n-1)+range(n-1,0,-1)

    for n,x in enumerate(text):
        fence[rail[n%len(rail)]][n]=x

    return (c for i in fence for c in i if c!= None)

print ''.join(fence('ATTACK.AT.DAWN',3))
