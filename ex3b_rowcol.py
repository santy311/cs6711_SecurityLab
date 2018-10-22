def col(text,key):
    table = [[None]*len(key) for i in range(len(text)/len(key))]
    for i in range(len(text)/len(key)):
        for j in range(len(key)):
            table[i][j]= text[i*len(key)+j]
    print table
    alpha ='abcdefghijklmnopqrstuvwxyz'
    cipher = ''
    for i in alpha:
        if key.find(i)!=-1:
            for row in range(len(text)/len(key)):
                cipher += table[row][key.find(i)]
    print cipher
    
x=col("hellohere123","zbc")
