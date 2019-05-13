cipher = {'a': 'y', 'e': 'i', 'i': 'o', 'o': 'a', 'y': 'e'}

def encode(plaintext,cipher=cipher) -> str:


    for ch in plaintext:
        if ch in cipher.keys():
           plaintext=plaintext.replace(ch,cipher.get(ch))
    return (plaintext)


cipherdev = {cipher[v]: v for v in cipher.keys()}

def decode(encoded,cipherdev=cipherdev):
    return encode(encoded,cipherdev)



'''def decode(encoded):

    cipherrev={'y':'a','i':'e','o':'i','a':'o','e':'y'}
    for i in encoded:
        if i in cipherrev.keys():
            encoded=encoded.replace(i,cipherrev.get(i))
    return (encoded)
'''




def main():


    plaintext = "hello foo"
    print(encode(plaintext,cipher))

    print(decode(encode(plaintext)))

if __name__ == '__main__':
    main()
