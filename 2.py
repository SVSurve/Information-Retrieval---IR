import numpy as np
from scipy.sparse import csc_matrix
def pageRank(G,s= .85, maxerr =.0001):
    n=G.shape[0]
    A =csc_matrix(G,dtype=np.float)
    rsums = np.array(A.sum(1))[:,0]
    ri, ci = A.nonzero()
    A.data /= rsums[ri]
    sink =rsums==0
    ro, r = np.zeros(n), np.ones(n)
    while np.sum(np.abs(r-ro)) > maxerr:
        ro = r.copy()
        for i in range(0,n):
            Ai=np.array(A[:,i].todense())[:,0]
            Di=sink/float(n)
            Ei=np.ones(n)/float(n)
            r[i] = ro.dot(Ai*s + Di*s +Ei*(1-s))
        return r/float(sum(r))

if __name__=='__main__':
    G=np.array([[0,0,1,0,0,0,0],
                [0,1,1,0,0,0,0],
                [1,0,1,1,0,0,0],
                [0,0,0,1,1,0,0],
                [0,0,0,0,0,0,1],
                [0,0,0,0,0,1,1],
                [0,0,0,1,1,0,1],])
    print(pageRank(G,s=.86))
