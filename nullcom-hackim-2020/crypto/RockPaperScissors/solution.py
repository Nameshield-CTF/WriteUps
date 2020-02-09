from Crypto.Util.number import *

from itertools import permutations

sbox = [221, 229, 120, 8, 119, 143, 33, 79, 22, 93, 239, 118, 130, 12, 63, 207, 90, 240, 199, 20, 181, 4, 139, 98, 78, 32, 94, 108, 100, 223, 1, 173, 220, 238, 217, 152, 62, 121, 117, 132, 2, 55, 125, 6, 34, 201, 254, 0, 228, 48, 250, 193, 147, 248, 89, 127, 174, 210, 57, 38, 216, 225, 43, 15, 142, 66, 70, 177, 237, 169, 67, 192, 30, 236, 131, 158, 136, 159, 9, 148, 103, 179, 141, 11, 46, 234, 36, 18, 191, 52, 231, 23, 88, 145, 101, 17, 74, 44, 122, 75, 235, 175, 54, 40, 27, 109, 73, 202, 129, 215, 83, 186, 7, 163, 29, 115, 243, 13, 105, 184, 68, 124, 189, 39, 140, 138, 165, 219, 161, 150, 59, 233, 208, 226, 176, 144, 113, 146, 19, 224, 111, 126, 222, 178, 47, 252, 99, 87, 134, 249, 69, 198, 164, 203, 194, 170, 26, 137, 204, 157, 180, 168, 162, 56, 81, 253, 213, 45, 21, 58, 24, 171, 37, 82, 53, 50, 84, 196, 232, 242, 244, 64, 80, 10, 114, 212, 187, 205, 28, 51, 182, 16, 107, 245, 211, 85, 92, 195, 5, 197, 200, 31, 183, 61, 123, 86, 167, 154, 41, 151, 35, 247, 246, 153, 95, 206, 149, 76, 112, 71, 230, 106, 188, 172, 241, 72, 156, 49, 14, 214, 155, 110, 102, 116, 128, 160, 135, 104, 77, 91, 190, 60, 42, 185, 96, 97, 251, 218, 133, 209, 65, 227, 3, 166, 255, 25]
p = [5, 9, 1, 8, 3, 11, 0, 12, 7, 4, 14, 13, 10, 15, 6, 2]
p2 = [6, 2, 15, 4, 9, 0, 14, 8, 3, 1, 12, 5, 7, 11, 10, 13]
round = 16

def repeated_xor(p, k):
    return bytearray([p[i] ^ k[i % len(k)] for i in range(len(p))])

def dehash(data, action):
    
    padded_option = bytearray(str.encode(action)) + bytearray(b'\x0f') * 15
    state = long_to_bytes(int(data, 16))
    for i in range(16):
        temp = bytearray(16)
	# Reverse shuffle
        for i in range(len(state)):
            temp[p2[i]] = state[i]
        state = temp
	# Reverse substitution
        for i in range(len(state)):
            state[i] = sbox.index(state[i])
	# Reverse XOR
        state = repeated_xor(state, padded_option)
    return state

def solution(option1, option2, option3):
    perm = permutations(['r','p','s'])
    for p in list(perm):
        res1 = dehash(option1, p[0])
        res2 = dehash(option2, p[1])
        res3 = dehash(option3, p[2])
	# If secret is the same for all 3
        if(res1 == res2 and res2 == res3):
            if(p[0] == 'r'):
                print('p')
            elif(p[0] == 'p'):
                print('s')
            else:
                print('r')
