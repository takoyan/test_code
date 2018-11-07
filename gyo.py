#encoding:UTF-8

import numpy as np
import scipy.linalg


def EigenValue():

    #固有値をいくつ求めるかを設定する
    hi = 2
    lo = 0

    #適当な行列を作る　
    A = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
    X=np.matrix([[-1, -np.sqrt(2)], [-1, 0], [1,0], [1, np.sqrt(2)]])

    SX=X.reshape(-1,)
    print(SX)
    #固有値、固有ベクトルを計算
    eigen_value,eigen_vector = np.linalg.eig(A)
    print(np.cov(A, rowvar=0, bias=1))
    print(eigen_value)
    print(eigen_vector)

    
    
    for i in range(len(eigen_vector)):
        eigen_vector[i]=eigen_vector[i]/np.linalg.norm(eigen_vector[i])
    
    print eigen_value
    print eigen_vector

if __name__=="__main__":
    EigenValue()
