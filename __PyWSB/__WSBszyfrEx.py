print('First module name is {}'.format(__name__))

if __name__=="__main__":
    cipher={'a':'o','e':'i'}

    cipherdev={cipher[v]: v for v in cipher.keys()}


    print(cipherdev)




