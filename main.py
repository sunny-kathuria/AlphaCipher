alpha="abcdefghijklmnopqrstuvwxyz"

def encrypt(s,shift=3):
    encrypted_str=""
    for c in s:
        index=alpha.index(c)
        shifted_index= (index+shift)%len(alpha)
        encrypted_str+=alpha[shifted_index]
    return encrypted_str
def decrypt(s,shift=3):
    decrypted_str=""
    for c in s:
        index=alpha.index(c)
        shifted_index=(index-shift)%len(alpha)
        decrypted_str+=alpha[shifted_index]
    return decrypted_str


#print(encrypt("heeeyyyyyyy"))
print(decrypt(encrypt("heeeyyyyyyy")))