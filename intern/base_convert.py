import base64 
from unicodedata import decimal
import codecs
import string
text ='MDAxMTAwMTEwMDExMDExMTAwMTEwMDExMDAxMTAwMTAwMDExMDAxMTAwMTExMDAwMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTEwMDEwMDAxMTAwMTEwMDExMDAwMDAwMTEwMDExMDAxMTAxMDAwMDExMDAxMTAwMTExMDAwMDAxMTAwMTEwMDExMDExMTAwMTEwMDExMDAxMTAwMTAwMDExMDAxMTAwMTEwMTAwMDAxMTAwMTEwMDExMTAwMDAwMTEwMDExMDAxMTAxMTEwMDExMDAxMTAwMTEwMDExMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTAxMDEwMDExMDAxMTAwMTEwMTExMDAxMTAwMTEwMDExMDExMDAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTEwMDAxMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTAxMTAwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMDAwMTAwMTEwMDExMDAxMTAwMDAwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTAwMDAwMDExMDAxMTAwMTEwMTAwMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTAxMDEwMDExMDAxMTAwMTEwMTExMDAxMTAwMTEwMDExMDAwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTAwMDAwMDExMDAxMTAwMTExMDAwMDAxMTAwMTEwMDExMDEwMDAwMTEwMDExMDAxMTAxMDEwMDExMDAxMTAwMTEwMDExMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTAwMDAwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMDAwMDAwMTEwMDExMDAxMTAxMDEwMDExMDAxMTAwMTEwMDAxMDAxMTAwMTEwMDExMTAwMDAwMTEwMDExMDAxMTAxMTEwMDExMDAxMTAwMTEwMTAwMDAxMTAwMTEwMDExMTAwMDAwMTEwMDExMDAxMTEwMDEwMDExMDAxMTAwMTEwMDAwMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTExMDAwMDAxMTAwMTEwMDExMDExMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTEwMDAxMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTEwMDEwMDExMDAxMTAwMTEwMDAwMDAxMTAwMTEwMDExMDAwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMDExMTAwMTEwMDExMDAxMTAxMTAwMDExMDAxMTAwMTEwMTAwMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTEwMDEwMDExMDAxMTAwMTEwMDAwMDAxMTAwMTEwMDExMDAwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMTAwMDAwMTEwMDExMDAxMTAxMTEwMDExMDAxMTAwMTEwMTAxMDAxMTAwMTEwMDExMDExMQ=='

def decodeBase64(base64_decode):
    text=base64.b64decode(base64_decode) 
    bi=(str(text)).strip("b'")#b'00110011=>00110011
    return bi
def Binary_to_Hex(text):
    mess = hex(int(text,2))#convert binary to hex
    #print(mess)
    hexValue=''
    for i in range(2,len(mess),4):#0x33 37 33 32 33 383335333=>373238
       hexValue += mess[i+2:i+4]
    return hexValue
def Hex_to_Decimal(text):
    hexValue=str (text)
    decValue=''
    for i in range(1,len(hexValue),2):#37323835313230=>72 85 120
       decValue += hexValue[i]
    return decValue
  
def DecodeRot13(text):
    decValue=str(text)
    fromDec = ''
    i=0
    while i< len(decValue):
        num = decValue[i:i+2]
        if int(num)>=32 :
            fromDec+=chr(int(num))
            i+=2
        else:
            num=decValue[i:i+3]
            fromDec+=chr(int(num))
            i+=3
    #print(Rot13)
    rot13trans =str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                              'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
    return fromDec.translate(rot13trans)
#def decodeBase64(text):


if __name__ =='__main__' : 
    bi=decodeBase64(text)
    # print(bi)
    hex=Binary_to_Hex(bi)
    dec=Hex_to_Decimal(hex)
    print(dec)
    rot13=DecodeRot13(dec)
    flag =(decodeBase64(rot13))
    print(flag)
    










# import base64
# import codecs
# import math

# def hextobinary(hex_string):
#     s = int(hex_string, 16) 
#     num_digits = int(math.ceil(math.log(s) / math.log(2)))
#     digit_lst = ['0'] * num_digits
#     idx = num_digits
#     while s > 0:
#         idx -= 1
#         if s % 2 == 1: digit_lst[idx] = '1'
#         s = s / 2
#     return ''.join(digit_lst)



# base64 = 'MDAxMTAwMTEwMDExMDExMTAwMTEwMDExMDAxMTAwMTAwMDExMDAxMTAwMTExMDAwMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTEwMDEwMDAxMTAwMTEwMDExMDAwMDAwMTEwMDExMDAxMTAxMDAwMDExMDAxMTAwMTExMDAwMDAxMTAwMTEwMDExMDExMTAwMTEwMDExMDAxMTAwMTAwMDExMDAxMTAwMTEwMTAwMDAxMTAwMTEwMDExMTAwMDAwMTEwMDExMDAxMTAxMTEwMDExMDAxMTAwMTEwMDExMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTAxMDEwMDExMDAxMTAwMTEwMTExMDAxMTAwMTEwMDExMDExMDAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTEwMDAxMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTAxMTAwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMDAwMTAwMTEwMDExMDAxMTAwMDAwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTAwMDAwMDExMDAxMTAwMTEwMTAwMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTAxMDEwMDExMDAxMTAwMTEwMTExMDAxMTAwMTEwMDExMDAwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTAwMDAwMDExMDAxMTAwMTExMDAwMDAxMTAwMTEwMDExMDEwMDAwMTEwMDExMDAxMTAxMDEwMDExMDAxMTAwMTEwMDExMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTAwMDAwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMDAwMDAwMTEwMDExMDAxMTAxMDEwMDExMDAxMTAwMTEwMDAxMDAxMTAwMTEwMDExMTAwMDAwMTEwMDExMDAxMTAxMTEwMDExMDAxMTAwMTEwMTAwMDAxMTAwMTEwMDExMTAwMDAwMTEwMDExMDAxMTEwMDEwMDExMDAxMTAwMTEwMDAwMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTExMDAwMDAxMTAwMTEwMDExMDExMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTEwMDAxMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTEwMDEwMDExMDAxMTAwMTEwMDAwMDAxMTAwMTEwMDExMDAwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMDExMTAwMTEwMDExMDAxMTAxMTAwMDExMDAxMTAwMTEwMTAwMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTEwMDEwMDExMDAxMTAwMTEwMDAwMDAxMTAwMTEwMDExMDAwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMTAwMDAwMTEwMDExMDAxMTAxMTEwMDExMDAxMTAwMTEwMTAxMDAxMTAwMTEwMDExMDExMQ'
# rot13 = codecs.encode(base64, 'rot_13')
# str = ''
# for i in rot13:
#     i = ord(i)
#     i = hex(i)
#     i = hextobinary(i)
#     str += i
# print(str)