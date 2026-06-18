import numpy as np
def is_diagonally_dominant(A):
    A=np.array(A,dtype=float)

    for i in range(A.shape[0]):
        diagonal=abs(A[i][i])
        others=np.sum(np.abs(A[i]))-diagonal
        if diagonal<others:
            return False
    return True    


def jacobi(A, b, x0=None, tol=1e-6, max_iter=100, verbose=False):
    """
    使用 Jacobi 迭代法求解线性方程组 A x = b。

    参数
    ----
    A : 二维数组，形状为 (n, n)
        系数矩阵。
    b : 一维数组，形状为 (n,)
        常数项向量。
    x0 : 一维数组，形状为 (n,)，可选
        初始迭代值。如果不传入，则默认使用全 0 向量。
    tol : 浮点数
        误差小于 tol 时停止迭代。
    max_iter : 整数
        最大迭代次数。
    verbose : 布尔值
        为 True 时打印每次迭代结果。

    返回值
    ------
    x : 数组
        方程组的近似解。
    iterations : 整数
        实际迭代次数。
    error : 浮点数
        最终误差。
    """
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("A 必须是方阵。")
    if not is_diagonally_dominant(A):
        print("警告：当前矩阵不满足主对角占优，Jocobi迭代法可能不收敛。")

    n = A.shape[0]
    if b.shape != (n,):
        raise ValueError("b 必须是一维向量，并且长度要和 A 的阶数相同。")

    diagonal = np.diag(A)
    if np.any(diagonal == 0):
        raise ValueError("Jacobi 迭代法不能处理主对角线上有 0 的矩阵。")

    if x0 is None:
        x = np.zeros(n)
    else:
        x = np.array(x0, dtype=float)
        if x.shape != (n,):
            raise ValueError("x0 的长度必须和 b 相同。")

    remainder = A - np.diagflat(diagonal)

    for iteration in range(1, max_iter + 1):
        x_new = (b - np.dot(remainder, x)) / diagonal
        error = np.max(np.abs(x_new - x))

        if verbose:
            print(f"第 {iteration} 次迭代: x = {x_new}, error = {error}")

        x = x_new
        if error < tol:
            return x, iteration, error

    return x, max_iter, error


if __name__ == "__main__":
    A = [
       [4,1],
       [1,5]
    ]
    b = [6,9]

    result, iterations, error = jacobi(A, b, tol=1e-3, verbose=True)
    print(f"近似解: {result}")
    print(f"迭代次数: {iterations}")
    print(f"最终误差: {error}")
