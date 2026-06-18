import numpy as np
def jacobi(A,b,tol=1e-6,max_iter=100):
    A=np.array(A,dtype=float)
    b=np.array(b,dtype=float)
    n=len(b)
    x=np.zeros(n)
    for k in range(max_iter):
        old_x=x.copy()
        for i in range(n):
            s=0
            for j in range(n):
                if i!=j:
                  s+=A[i][j]*old_x[j]
            x[i]=(b[i]-s)/A[i][i]
            error=np.max(np.abs(x-old_x))
        print(f"第{k+1}次迭代:{x},error={error}")
        if error<tol:
          return x
    return x
A = [
    [2, 1],
    [1, 4],
]

b = [5, 6]
result=jacobi(A,b)
print("最终结果：",result)    
