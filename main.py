# ===============  ASSIGNMENT 1 ===================

### 1. Write the Python codes for encoding a phrase in a number and decoding the number to the text : convert a text to number , save to a file (binary or text), and convert a number (from a given file) to text.


def encode(s):
    s = str(s)  # making input a string
    return sum(ord(s[i]) * 2048**i for i in range(len(s)))


def decode(n):
    n = int(n)  # making input an integer
    v = []
    while n != 0:
        v.append(chr(n % 2048))
        n //= 2048  # this replace n by floor (n/1024)
    return ''.join(v)


print("=====Question 1- Answer =====")
p = 'convert a text to number, save to a file (binary or text), and convert a number (from a given file) to text.'
print('Original Phrase: ' + p)
print('1. Encoded the original phrase to the following numbers:')
e = encode(p)
print(e)
print('2. Then, decoded the above numebers to the following:')
d = decode(e)
print(d)
#
# save to file : encoded.txt
#

file = open('\Directory', 'e', encoding='utf-8')
file.write(str(encode(p)))
file.close()

# ### 2. Write the Python codes for the Caesar encryption (save the Cipher text to a file) and decryption (read the Cipher text from a given file).

# #
# #--------------------- Caesar encryption & decryption -----------------
# #
# def encode(s,k):
#     s=str(s) # making input a string
#     n=sum(((ord(s[i])+ k) % 256)*256^i for i in range (len(s)))
#     v=[]
#     while n != 0 :
#         v.append(chr(n % 256))
#         n //=256  # this replace n by floor(n/256)
#     return ''.join(v)
# #
# # ----------------------------------------------------------
# #
# def decode(s,k):
#     s=str(s) # making input a string
#     n=sum((ord(s[i]) % 256)*256^i for i in range (len(s)))
#     v=[]
#     while n != 0 :
#         m= ((n % 256)+ 256-k) % 256
#         v.append(chr(m))
#         n //=256  # this replace n by floor(n/256)
#     return ''.join(v)
# #
# # ----------------------------------------------------------
# #
# P='Someday there will be a new world of shining hope for your family, your fatherland and your mankind'
# # Choose k = the number of positions for shifting , for example, let k=13
# C=encode(P,13)
# print('The Cipher text now is : ')
# print(C)
# print( )
# print(' Decryption -  get back the original Plaintext : ')
# P1=decode(C,13)
# print(P1)

# ### 3. Write the Python codes for the Exponential (Deffie-Hellman) encryption (save the Cipher text to a file) and decryption (read the Cipher text from a given file).

# #----------------------------Exponential Encryption----------------------------
# #                         (Pohlig-Hellman Encryption)
# # (4 blocks-)
# #
# #  ( Add blanks if not divisible by 4)
# #
# #------------------------------------------------
# def encode1(s,e,p):
#     s=str(s) # making input a string
#     r1=sum(ord(s[i])*2048^i for i in range (len(s)))
#     r2=power_mod(r1,e,p)
#     return r2
# #-------------------------------------------------
# def decode1(m,d,p):
#     n=power_mod(m,d,p)
#     n=Integer(n)
#     v=[]
#     while n != 0 :
#         v.append(chr(n % 2048))
#         n //=2048  # this replace n by floor (n/2048)
#     return ''.join(v)
# #-------------------------------------------------
# def encode(s,e,p):
#     s=str(s) # making input a string
#     L=[]
#     PL=[]
# #
#     if len(s) % 4== 1 :
#         s+='   '    # add to s three blanks
#     if len(s) % 4== 2 :
#         s+='  '     # add to s two blanks
#     if len(s) % 4== 3:
#         s+=' '     # add to s one blanks
# #
#     n=len(s)/4-1
#     for i in [0..n]:
#         k=4*i
#         PL.append(s[k:k+4])
# #
#     for i in range (0,len(PL)):
#         r=encode1(PL[i],e,p)
#         L.append(r)
#     return L
# #-------------------------------------------------
# def decode(L,d,p):
#     PL=[]
#     for i in range (0,len(L)):
#         r=decode1(L[i],d,p)
#         PL.append(r)
#     return ''.join(PL)
# #------------------------------------------------------
# #
# p=next_prime(17^125+11)
# e=next_prime(13^15+2)
# # The key of the encryption : (e,p)  (Keep secrete, at least keep e !)
# d=inverse_mod(e,p-1)
# # The key of the decryption : (d,p)  (Keep secrete, at least keep d !)
# P1='словами не передать, как я тебя люблю'  # Test
# print(' The plain text : ')
# print(P1)
# print( )
# C=encode(P1,e,p)
# print(' Encryption - The Cipher text : ')
# print(C)
# print( )
# print(' Decryption - get back the orignal plain text : ')
# P2=decode(C,d,p)
# print(P2)

# ### ASSIGNMENT 2
# 1. Write the Python codes for the RSA encryption (save the Cipher text to a file)
# and decryption (read the Cipher text from a given file).
# 2. Write the Python codes for the RSA with digital signature encryption (save the
# Cipher text and digital signature to file(s) ) and decryption (read the Cipher
# text and digital signature from given file(s) ).
# 3. Write the Python codes for the Elgamal encryption (save the Cipher text to a file)
# and decryption (read the Cipher text from a given file).
