#Code By Binyamin Alony, id = 324861228

def Remainder(A, B, isDecode = False):
    order = len(B)                                                              # order of B
    remainder = StripOfZeros([i for i in A])                                    # initialize the remainder to be M stripped of zeros
    if not isDecode:                                                            # unless we're decoding, add the 0^order at the end of M
        remainder = remainder + ['0' for i in range(order-1)]
    #print(''.join(remainder))
    while len(remainder) >= order:                                              # while the remainder is bigger than M:
        for i in range(len(B)):
            try:                                                                
                remainder[i] = xor(remainder[i],B[i])                           # for every bit, xor remainder and B
            except:
                print(i)                                                        # try-except - for debugging purposes
                return '-1'
        remainder = StripOfZeros(remainder)                                     # strip remainder of zeros
        #print(''.join(remainder))
        #print(''.join([i for i in B]))
    return ''.join(remainder)                                                   # return the remainder as a string

def StripOfZeros(A):                                                            # strip zeros: removing 0's untill A[0] is 1
    while len(A) >= 1 and A[0] == '0':
        A = A[1:]
    return A

def xor(A,B):                                                                   # xor = bit equality
    if A==B:
        return '0'
    return '1'

def JoinAndPadWithZeros(M,G, remainder):                                        # pad the remainder with zeros until it's G's length, and join with A
    lenToPad = len(G)-len(remainder)
    if lenToPad<=0:
        return M+remainder
    return M+''.join(['0' for _ in range(lenToPad)])+remainder
    
def CRC(M, G):                                                                  # calculate the remainder and join it to A.
    return (JoinAndPadWithZeros(M, G, Remainder(M,G)))




# question 3
G = '10011'
print(CRC('1010101010',G))
print(CRC('1001010101',G))
print(CRC('0101101010',G))
print(CRC('1010100000',G))
