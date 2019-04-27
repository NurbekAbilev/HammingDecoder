from itertools import zip_longest

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def code_hamming(binary_string):
    blocks = []
    blocks = list(grouper(binary_string,4,""))
    blocks = [list(item) for item in blocks]
    for i in range(len(blocks)):
        blocks[i] = code_block([int('0'+val) for val in blocks[i]])

    return blocks
    
def code_block(b):
    if(len(b)!=4):
        print("Block must be of length 4")
        return None
    r1 = b[0]^b[1]^b[2]
    r2 = b[1]^b[2]^b[3]
    r3 = b[0]^b[1]^b[3]
    return b + [r1,r2,r3]

import random
def random_noise(blocks): # len(blocks) = 7
    for i in range(len(blocks)):
        rand = random.randint(0,6)
        if(blocks[i][rand] == 0):
            blocks[i][rand] = 1
        else:
            blocks[i][rand] = 0
    return blocks

def decode_hamming(binary_arr):
    for i in range(len(binary_arr)):
        binary_arr[i] = decode_block(binary_arr[i])

    return binary_arr

def decode_block(b): #detect error and recover
    s1 = b[4]^b[0]^b[1]^b[2]
    s2 = b[5]^b[1]^b[2]^b[3]
    s3 = b[6]^b[0]^b[1]^b[3]
    
    error_bit = get_error_bit(s1,s2,s3)
    # print(error_bit)
    # print(b[error_bit])
    b[error_bit] = reverse(b[error_bit])
    # print(b[error_bit])
    
    return b

def reverse(bit):
    if(bit == 0):
        return 1
    else:
        return 0

def get_error_bit(s1,s2,s3):
    s = str(s1)+str(s2)+str(s3)
    num = int(s,2)
    if(num==1):
        return 6
    if(num==2):
        return 5
    if(num==3):
        return 3
    if(num==4):
        return 4
    if(num==5):
        return 0
    if(num==6):
        return 2
    if(num==7):
        return 1
    
    print("Error")

