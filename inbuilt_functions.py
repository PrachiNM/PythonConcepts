def encrypt(string, factor):
    stringx = ''
    for x in range(len(string)):
        enc = ord(string[x])+factor
        if enc - ord('a')+1 > 26:
            enc = ((enc-ord('a')) % 26) + ord('a')
        stringx += chr(enc)
    return stringx


print(encrypt('asz', 2))
