import numpy as np

# simplex algorithm
# An : 2d array constraint matrix
# c : 1d array  factor c * x
# b : 1d array  constraint vector
# B : 1d array of base vars indices
# N : 1d array of non-base vars indices
def simplex(An, c, b, N, B):
    x = np.concatenate((np.zeros(len(N)), b))
    c = np.concatenate((c, np.zeros(len(B))))
    A = np.concatenate((An, np.eye(len(An))), axis=1)
    it = 0
    while True:
        print(20*"-")
        print("Iteration No. ", it)
        print("N = ", N)
        print("B = ", B)
        it += 1
        cb = np.array(c[B])
        y = np.linalg.solve(A[:,B].T, cb) 
        cn = np.array(c[N], dtype='float64')
        cn -= np.matmul(A[:,N].T, y)
        print("cN = ", cn)
        if np.all(np.less_equal(cn, np.zeros(cn.shape))):
            print("Finished")
            print("x = ",x)
            exit()

        j = -1
        for i in N:
            if(c[i] > 0):
                j = i
                print("selected j = ", j)
                break

        if j < 0: exit()

        w = np.linalg.solve(A[:,B], A[:,j])
        if np.all(np.less_equal(w, np.zeros(w.shape))):
            print("Unbounded")
            exit()

        t = np.amin(x[B]/w)
        idx = np.argmin(x[B]/w) + len(N)
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


B = [2,3,4]
N = [0,1]
b = [120,160,43]
c = [5,4]
muesli = [
        [2,3],
        [4,1],
        [1,1],
        ]

if __name__ == '__main__':
    simplex(muesli, c, b, N, B)
