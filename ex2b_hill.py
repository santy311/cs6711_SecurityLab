def genmat(key,n):
    table = [[0]*n for row in range(n)]
    for i in range(n):
        for j in range(n):
            table[i][j] = ord(key[i*n+j])-97
    #print table
    return table

def hill(text,key):
    table = genmat(key,len(text))
    keymat = [ord(i)-97 for i in text]
    print keymat
    for row in range(len(text)):
        temp = 0
        for j in range(len(text)):
            temp += table[row][j]*keymat[j]
        print chr(temp%26+97)

hill('act','gybnqkurp')
