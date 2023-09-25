def find_median(A):
    _min = min(A)
    _max = max(A)
    for i in range(3):
        if A[i] != _min and A[i] != _max:
            return A[i]

def choose_pivot(A,flag):
    n = len(A)
    first = A[0]
    final = A[n-1]
    if n % 2 == True:
        k = int(n/2)
        middle = A[k]
    elif n % 2 != True:
        k = int(n/2) - 1
        middle = A[k]
    else:
        print('err choose_pivot middle')

    B = [first,middle,final]
    med = find_median(B)
    if med == B[0]:
        position = 0
    elif med == B[1]:
        position = k
    else:
        position = n-1

    if flag == 1:
        return 0
    if flag == 2:
        return n-1
    if flag == 3:
        return position
    else:
        print('err choose_pivot flag')

def swap(A, first, second):
    second_value = A[second]
    first_value = A[first]
    A[first] = second_value
    A[second] = first_value
    return A

def partition(A):
    pivot = A[0]
    r = len(A)
    i = 1
    for j in range(1,r):
        if A[j] < pivot:
            A = swap(A,i,j)
            i += 1
    A = swap(A, 0, i-1)
    return A,i-1

def quick_sort(A,flag):
    n = len(A)
    if n > 1:
        p = choose_pivot(A,flag)
        A = swap(A,0,p)
        A,pivot_position = partition(A)
        A[:pivot_position],left = quick_sort(A[:pivot_position],flag)
        A[pivot_position+1:],right = quick_sort(A[pivot_position+1:],flag)
        return A, left+right+n-1
    else:
        return A, 0

with open('./content/quick_sort.txt') as f:
    a = [int(x) for x in f]

print(quick_sort(a, 2))
