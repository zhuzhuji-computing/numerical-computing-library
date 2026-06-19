# Jacobi 迭代法用户使用说明

本文档说明如何使用 `jacobi.py` 中的 `jacobi` 函数求解线性方程组。

Jacobi 迭代法用于求解形如：

```text
A x = b
```

的线性方程组。

其中：

- `A` 是系数矩阵
- `b` 是常数项向量
- `x` 是要求解的未知数向量

## 运行环境

使用前需要安装 Python 和 NumPy。

安装 NumPy：

```bash
pip install numpy
```

## 文件说明

当前函数位于：

```text
jacobi.py
```

主要包含两个函数：

```python
is_diagonally_dominant(A)
```

用于判断矩阵是否主对角占优。

```python
jacobi(A, b, x0=None, tol=1e-6, max_iter=100, verbose=False, check=True)
```

用于使用 Jacobi 迭代法求解线性方程组。

## 基本使用方法

新建一个 Python 文件，例如 `test_jacobi.py`，写入：

```python
from jacobi import jacobi

A = [
    [2, 1],
    [1, 4],
]

b = [5, 6]

result, iterations, error = jacobi(A, b)

print("最终结果：", result)
print("迭代次数：", iterations)
print("最终误差：", error)
```

运行：

```bash
python test_jacobi.py
```

输出结果大约为：

```text
最终结果： [1.99999988 0.99999994]
迭代次数： 16
最终误差： 3.5762786865234375e-07
```

也就是说，方程组的近似解为：

```text
x ≈ 2
y ≈ 1
```

## 如何把方程组写成 A 和 b

例如有方程组：

```text
2x + y = 5
x + 4y = 6
```

对应的系数矩阵和常数项向量是：

```python
A = [
    [2, 1],
    [1, 4],
]

b = [5, 6]
```

再比如三元线性方程组：

```text
10x + 2y + z = 13
x + 8y - z = 6
2x - y + 5z = 9
```

可以写成：

```python
A = [
    [10, 2, 1],
    [1, 8, -1],
    [2, -1, 5],
]

b = [13, 6, 9]
```

## 参数说明

函数定义：

```python
jacobi(A, b, x0=None, tol=1e-6, max_iter=100, verbose=False, check=True)
```

### A

系数矩阵，必须是方阵。

例如：

```python
A = [
    [2, 1],
    [1, 4],
]
```

### b

常数项向量，长度必须和 `A` 的阶数相同。

例如：

```python
b = [5, 6]
```

### x0

初始迭代值。

如果不传入，默认使用全 0 向量。

例如：

```python
result, iterations, error = jacobi(A, b, x0=[1, 1])
```

### tol

误差精度。

当新旧两次迭代结果的最大差值小于 `tol` 时，停止迭代。

默认值：

```python
tol=1e-6
```

也就是：

```text
0.000001
```

例如：

```python
result, iterations, error = jacobi(A, b, tol=1e-3)
```

### max_iter

最大迭代次数。

如果迭代次数达到 `max_iter`，即使误差还没有小于 `tol`，也会停止。

例如：

```python
result, iterations, error = jacobi(A, b, max_iter=50)
```

### verbose

是否显示每一次迭代过程。

默认：

```python
verbose=False
```

不显示每轮迭代。

如果想观察每一轮计算结果，可以写：

```python
result, iterations, error = jacobi(A, b, verbose=True)
```

### check

是否检查矩阵是否主对角占优。

默认：

```python
check=True
```

如果矩阵不满足主对角占优，会输出警告：

```text
警告：当前矩阵不满足主对角占优，Jacobi 迭代法可能不收敛。
```

如果不想检查，可以写：

```python
result, iterations, error = jacobi(A, b, check=False)
```

## 返回值说明

`jacobi` 函数返回三个值：

```python
result, iterations, error = jacobi(A, b)
```

### result

最终得到的近似解。

例如：

```text
[1.99999988 0.99999994]
```

### iterations

实际迭代次数。

例如：

```text
16
```

### error

最终误差。

例如：

```text
3.5762786865234375e-07
```

## 直接运行 jacobi.py

也可以直接运行：

```bash
python jacobi.py
```

此时会运行文件底部的示例代码。

因为示例代码写在：

```python
if __name__ == "__main__":
```

下面，所以当其他文件导入 `jacobi` 函数时，示例代码不会自动执行。

## 常见错误

### A 不是方阵

错误示例：

```python
A = [
    [1, 2, 3],
    [4, 5, 6],
]
```

这不是方阵，会报错：

```text
A 必须是方阵。
```

### b 的长度不匹配

错误示例：

```python
A = [
    [2, 1],
    [1, 4],
]

b = [5, 6, 7]
```

`A` 是二阶矩阵，但 `b` 有 3 个数，会报错：

```text
b 必须是一维向量，并且长度要和 A 的阶数相同。
```

### 主对角线上有 0

错误示例：

```python
A = [
    [0, 1],
    [1, 4],
]
```

Jacobi 迭代公式中需要除以主对角线元素，所以主对角线上不能有 0。

会报错：

```text
A 的主对角线上不能有 0。
```

### 矩阵不主对角占优

如果矩阵不满足主对角占优，Jacobi 迭代法可能不收敛。

例如：

```python
A = [
    [1, 5],
    [4, 1],
]
```

这时程序会给出警告。

可以尝试交换方程顺序，让较大的系数放到主对角线上：

```python
A = [
    [4, 1],
    [1, 5],
]
```

## 完整示例

```python
from jacobi import jacobi

A = [
    [10, 2, 1],
    [1, 8, -1],
    [2, -1, 5],
]

b = [13, 6, 9]

result, iterations, error = jacobi(
    A,
    b,
    tol=1e-6,
    max_iter=100,
    verbose=True,
)

print("最终结果：", result)
print("迭代次数：", iterations)
print("最终误差：", error)
```

## 注意事项

Jacobi 迭代法不是所有线性方程组都一定收敛。

通常情况下，如果系数矩阵满足主对角占优，Jacobi 迭代法更容易收敛。

如果结果发散或者误差越来越大，可以先检查：

- 方程组是否写成了正确的 `A` 和 `b`
- 主对角线上是否有 0
- 是否可以交换方程顺序，让矩阵主对角占优
- `tol` 是否设置得过小
- `max_iter` 是否设置得过小
