import numpy as np
A=np.array([[10,3,1],[2,-10,3],[1,3,10]])
b=np.array([14,-5,14])
n=len(b)
x=np.zeros(n)
error=1.0
def Jacobi(A,b,x,n,error):
    max_iter=100
    counter=0
    while error>1e-3 and counter < max_iter:
        y=x.copy()
        for i in range(n):
            s1=0
            for j in range(n):
                if i!=j:
                    s1+=A[i][j]*y[j]
            x[i]=(b[i]-s1)/A[i][i]
        # 计算误差（取前后两次迭代差异最大的那个分量）
        error = np.max(np.abs(x - y))
        counter += 1
        print(f"第{counter}次迭代: {x}")

    return x
result = Jacobi(A, b, x, n, error)