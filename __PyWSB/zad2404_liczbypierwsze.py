pierwsze_skl=[]



def pierwsza_funk(n):
    pierwsze=[]
    for x in range(2,n):
        for k in pierwsze:
            if x%k==0: break
        else:
            yield x
            pierwsze.append(x)
    return pierwsze

print(pierwsza_funk(25))

'''for x in pierwsza_funk(13):
   print(x)'''

