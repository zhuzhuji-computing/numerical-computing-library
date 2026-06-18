# 数值计算与运筹优化函数库

这是一个用 Python 编写的数值计算与运筹优化函数库项目。

本项目的目标是把我在大学阶段学习过的 **数值计算**、**运筹学**、**优化方法** 等知识整理成可以直接调用的 Python 函数，最终做成类似 MATLAB 工具箱的效果。

我希望这个项目不只是一个代码仓库，而是一个长期积累型的学习项目。通过亲手实现这些算法，把课堂上的数学理论、算法思想和编程实践真正连接起来。

## 项目简介

目前这个项目还处于初始阶段。

我会先从已经学过或者正在学习的内容开始，把一个个算法逐步写成 Python 函数，并配上必要的示例和说明。

未来希望可以像这样调用：

```python
from numoptkit.numerical.linear_systems import jacobi
from numoptkit.numerical.ode import rk4
from numoptkit.optimization.integer_programming import branch_and_bound
```

也就是说，最终希望它能够成为一个可以直接 `import` 使用的个人数学计算工具箱。

## 项目目标

这个项目主要有以下几个目标：

1. 把课堂上学过的数学算法真正写成代码；
2. 建立一个可以长期积累和复用的 Python 工具库；
3. 通过代码加深对数值计算、运筹学和优化方法的理解；
4. 训练自己的编程能力、项目管理能力和 GitHub 使用能力；
5. 为以后继续学习计算数学、优化算法和科学计算打基础。

## 当前已完成内容

目前项目中已经包含：

* Jacobi 迭代法

后续会继续在此基础上整理更多算法。

## 计划实现的内容

### 一、数值计算部分

计划实现的内容包括：

#### 1. 方程求根

* 二分法
* 牛顿法
* 割线法

#### 2. 线性方程组数值解法

* Jacobi 迭代法
* Gauss-Seidel 迭代法
* 高斯消元法
* LU 分解

#### 3. 插值与逼近

* 拉格朗日插值
* 牛顿插值
* 分段插值

#### 4. 数值积分

* 梯形公式
* 辛普森公式
* 复化求积公式

#### 5. 常微分方程数值解

* 欧拉法
* 改进欧拉法
* 四阶 Runge-Kutta 方法

### 二、运筹学与优化部分

计划实现的内容包括：

* 运输问题和分配问题
* 整数规划
* 对策论
* 无约束问题的下降算法与线性搜索
* 无约束问题算法
* 非线性方程组与最小二乘
* 约束问题解的最优性条件
* 二次规划
* 约束问题算法

目前这一部分先只列出主要方向，后续在具体学习和实现对应算法时，再逐步补充每一部分的小标题、算法说明、数学原理和代码示例。

## 项目结构规划

目前项目还在初始阶段，后续计划整理成如下结构：

```text
numerical-computing-library/
├── README.md
├── src/
│   └── numoptkit/
│       ├── __init__.py
│       ├── numerical/
│       │   ├── __init__.py
│       │   ├── root_finding.py
│       │   ├── linear_systems.py
│       │   ├── interpolation.py
│       │   ├── integration.py
│       │   └── ode.py
│       └── optimization/
│           ├── __init__.py
│           ├── transportation.py
│           ├── assignment.py
│           ├── integer_programming.py
│           ├── game_theory.py
│           ├── unconstrained_optimization.py
│           ├── nonlinear_equations.py
│           ├── least_squares.py
│           ├── optimality_conditions.py
│           ├── quadratic_programming.py
│           └── constrained_optimization.py
├── examples/
└── tests/
```

其中：

* `src/` 用来存放真正的函数库代码；
* `numoptkit/` 是未来计划使用的 Python 包名；
* `numerical/` 用来存放数值计算相关算法；
* `optimization/` 用来存放运筹学与优化相关算法；
* `examples/` 用来存放使用示例；
* `tests/` 用来存放测试代码，检查函数结果是否正确。

## 使用示例

例如，未来希望可以这样调用 Jacobi 迭代法：

```python
from numoptkit.numerical.linear_systems import jacobi

A = [
    [10, -1, 2],
    [-1, 11, -1],
    [2, -1, 10]
]

b = [6, 25, -11]

x = jacobi(A, b)

print(x)
```

也希望可以这样调用四阶 Runge-Kutta 方法：

```python
from numoptkit.numerical.ode import rk4

def f(x, y):
    return x + y

result = rk4(f, x0=0, y0=1, h=0.1, n=10)

print(result)
```

## 当前进度

* [x] 创建 GitHub 仓库
* [x] 上传第一个 Python 文件
* [x] 编写 README 文件
* [ ] 整理项目文件结构
* [ ] 完善 Jacobi 迭代法代码
* [ ] 添加数值计算相关算法
* [ ] 添加运筹学与优化相关算法
* [ ] 编写使用示例
* [ ] 添加测试代码
* [ ] 尝试整理成可以安装和调用的 Python 包

## 长期目标

这个项目的长期目标是建立一个属于自己的数学计算工具箱。

我希望它能够帮助我完成从“学过算法”到“实现算法”，再到“复用算法”的转化。

在未来的学习中，我会继续把数值计算、运筹学、优化算法、科学计算等方向的内容逐步加入这个项目中，使它成为一个长期维护和不断扩展的个人项目。

## 作者

zhuzhuji
