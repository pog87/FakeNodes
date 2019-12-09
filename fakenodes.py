import numpy as np
import numpy.matlib


def lebesgue(x, xx):
    L = np.abs( lagrange(x,xx) )
    return np.sum( L, axis = -1 )

def lagrange(x, xx):
    n=len(x); m=len(xx)
    L=np.zeros((m,n))
    for k in range(n):
        x_k = np.concatenate((x[:k],x[k+1:]))
        L[:,k] = np.prod(np.matlib.repmat(xx.reshape(m,1),1,n-1) - np.matlib.repmat(x_k,m,1) , axis=1) / np.prod(x[k]-x_k)
    return L

def lagrange_interp(x,y,xx):
    L = lagrange(x,xx)
    return np.dot(L,y)


def fakenodes_interp(x,y,xx,S=None, degree=None):
    if S is None:
        #perform tradictional interpolation
        S=lambda x:x
    if degree is None:
        degree=len(x)-1
    #
    x_=S(x); xx_ = S(xx)
    P=np.polyfit(x_,y,degree)
    yy=np.polyval(P,xx_)
    #yy=lagrange_interp(xx_,x_,y)
    return yy
