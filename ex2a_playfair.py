import re

def gentab(key=''):
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    table = [[0] * 5 for row in range(5)]

    key_set = list(sorted(set(key),key=key.index))
    total_set = key_set
    for i in alphabet:
        if i not in key_set:
            total_set.append(i)

    for i in range(5):
        for j in range(5):
            table[i][j]=total_set[i*5+j]
        print(table[i])
    return table


def find(searchList, elem):
    for i in range(5):
        for j in range(5):
            if elem == searchList[i][j]:
                return i,j


def enc(key,text):
        cipher = ''
        table = gentab(key)
        for i in range(0,len(text),2):
            x1,y1=find(table,text[i])
            x2,y2=find(table,text[i+1])
            print x1,y1,x2,y2
            if y1<y2:
                y3=y2
                y4=y1
            else:
                y3=y2
                y4=y1
            cipher+=table[x1][y3]
            cipher+=table[x2][y4]
        print cipher
        decode(key,cipher)
def decode(key,text):
    decf = ''
    table = gentab(key)
    for i in range(0,len(text),2):
        x1,y1=find(table,text[i])
        x2,y2=find(table,text[i+1])
        print x1,y1,x2,y2
        if y1<y2:
            y3=y2
            y4=y1
        else:
            y3=y2
            y4=y1
        decf+=table[x1][y3]
        decf+=table[x2][y4]
    print decf
enc('hello','hdmz')
