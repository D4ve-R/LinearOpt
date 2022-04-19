import numpy as np

# simplex algorithm
# An : 2d array constraint matrix
# c : 1d array  factor c * x
# b : 1d array  constraint vector
# max c * x
# s.t. An * x <= b
def simplex(An, c, b):
    n = len(c)
    m = len(b)
    N = list(np.arange(n))
    B = list(np.arange(n, n + m))
    x = np.concatenate((np.zeros(n), b))
    c = np.concatenate((c, np.zeros(m)))
    A = np.concatenate((An, np.eye(len(An))), axis=1)
    it = 0

    while True:
        print(20*"-")
        print("Iteration No. ", it)
        print("N = ", N)
        print("B = ", B)
        it += 1
        y = np.linalg.solve(A[:,B].T, c[B]) 
        cn = c[N] - np.matmul(A[:,N].T, y)
        print("cN = ", cn)

        if np.all(np.less_equal(cn, np.zeros(cn.shape))):
            print("Finished")
            print("x = ",x[np.arange(n)])
            exit()

        j = np.where(c == np.amax(c[N]))[0][0]
        print("selected j = ", j)

        w = np.linalg.solve(A[:,B], A[:,j])
        if np.all(np.less_equal(w, np.zeros(w.shape))):
            print("Unbounded")
            exit()

        t = np.amin(x[B]/w)
        idx = np.argmin(x[B]/w) + n
        print("selected i = ", idx)
        x[B] -= t * w
        x[j] = t
        N.append(idx)
        N.remove(j)
        B.append(j)
        B.remove(idx)
        N.sort()
        B.sort()
        #exit()


b = [120,160,43]
c = [5,4]
muesli = [
        [2,3],
        [4,1],
        [1,1],
        ]

b2 = [120,160,43,82]
muesli2 = [
        [2,3],
        [4,1],
        [1,1],
        [2,1]
        ]

test = [
        [2,-1,2,1,0,0,1,0,0],
        [-2,3,-1,0,-1,0,0,1,0],
        [1,-1,2,0,0,-1,0,0,1]
        ]
btest = [4,5,1]
ctest = [-1,-1,-1]

if __name__ == '__main__':
    simplex(test, ctest, btest)
