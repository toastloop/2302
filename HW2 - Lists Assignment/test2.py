import numpy as np

def diagonal(A):
    arr = []
    for i in range(A.shape[0]):
        arr.append(A[i][i])
    return np.array(arr)

def count_digits(A):
    count = np.zeros(10,dtype=np.int16)
    for i in range(10):
        if i in A:
            count[i] = np.count_nonzero(A == i)
    return count

print('Question 12')
np.random.seed(12)
for i in range(2,6):
    A = np.random.randint(0,10,size = (i,i))
    print('A = \n',A)
    print('diagonal(A) =',diagonal(A))

print('Question 13')
np.random.seed(13)
A1 = np.random.randint(0,10,size = 12)
A2 = np.random.randint(-9,10,size = 12)
A3 = np.random.randint(-15,16,size = (4,8))
A4 = np.random.randint(-15,16,size = (4,3,2))
for A in [A1,A2,A3,A4]:
    print('A = \n',A)
    print('count_digits(A) = ',count_digits(A))