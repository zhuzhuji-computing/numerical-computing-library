import numpy as np


class JacobiResult:
    def __init__(self, solution, iterations, error):
        self.solution = solution
        self.iterations = iterations
        self.error = error

    def __iter__(self):
        yield self.solution
        yield self.iterations
        yield self.error

    def __str__(self):
        return (
            f"最终结果：{self.solution}\n"
            f"迭代次数：{self.iterations}\n"
            f"最终误差：{self.error}"
        )

    def __repr__(self):
        return str(self)


def is_diagonally_dominant(A):
    A = np.array(A, dtype=float)

    for i in range(A.shape[0]):
        diagonal = abs(A[i][i])
        others = np.sum(np.abs(A[i])) - diagonal
        if diagonal < others:
            return False
    return True


def jacobi(A, b, x0=None, tol=1e-6, max_iter=100, verbose=False, check=True):
    """
    使用 Jacobi 迭代法求解线性方程组 A x = b。

    A 是系数矩阵，b 是常数项向量。
    默认从全 0 向量开始迭代，也可以通过 x0 指定初始值。
    """
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("A 必须是方阵。")

    n = A.shape[0]
    if b.shape != (n,):
        raise ValueError("b 必须是一维向量，并且长度要和 A 的阶数相同。")

    diagonal = np.diag(A)
    if np.any(diagonal == 0):
        raise ValueError("A 的主对角线上不能有 0。")

    if check and not is_diagonally_dominant(A):
        print("警告：当前矩阵不满足主对角占优，Jacobi 迭代法可能不收敛。")

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
            return JacobiResult(x, iteration, error)

    return JacobiResult(x, max_iter, error)


if __name__ == "__main__":
    A = [
        [2, 1],
        [1, 4],
    ]

    b = [5, 6]

    print(jacobi(A, b, verbose=True))
