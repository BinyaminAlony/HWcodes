#Code By Binyamin Alony, id = 324861228

def CRC(A, B, isDecode = False):
    order = len(B)
    remainder = StripOfZeros([i for i in A])
    if not isDecode:
        remainder = remainder + ['0' for i in range(order-1)]
    print(''.join(remainder))
    while len(remainder) >= order:
        for i in range(len(B)):
            try:
                remainder[i] = xor(remainder[i],B[i])
            except:
                print(i)
                return '-1'
        remainder = StripOfZeros(remainder)
        print(''.join(remainder))
        print(''.join([i for i in B]))
    return ''.join(remainder)

def StripOfZeros(A):
    while len(A) >= 1 and A[0] == '0':
        A = A[1:]
    return A

def xor(A,B):
    if A==B:
        return '0'
    return '1'


M = '10110'
M_dirty = '1001100110101010'
G = '1001'
print('remainder is: ' + CRC(M,G))
print(M+CRC(M,G))
#print(CRC(M_dirty,G, isDecode=True))
