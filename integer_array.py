with open('./content/integer_array.txt') as f:
    _input = [int(x) for x in f]

def cnt_split_inv(B,C):
    i = 0
    j = 0
    count = 0
    D = []
    while i<len(B) and j<len(C):
        D.extend([min(B[i],C[j])])
    if B[i] < C[j]:
        i = i + 1
    else:
        count +=len(B[i:])
        j+=1
    D.extend(B[i:])
    D.extend(C[j:])
    Z = count
    return D, Z

def sort_cnt(A):
    n = len(A)
    if n > 1:
        splitposition = int(n / 2)
        B,X = sort_cnt(A[:-splitposition])
        C,Y = sort_cnt(A[-splitposition:])
        D,Z = cnt_split_inv(B,C)
        return D, X+Y+Z
    else:
        return A, 0

print(sort_cnt(_input))
