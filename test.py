# 导入sympy库
from sympy import *

# 定义字符
a, b,  r, t = symbols('a b r t')

#将所有项移至左端，右端为零
eq1 = (sqrt(3)*(2*r+t)/4 - a)**2 + ((2*r+t)/4 - b)**2 - r**2
eq2 = (r - a)**2 + b**2 - r**2
eq3 = (sqrt(3)*(2*r-t)/4 - a)**2 + ((2*r-t)/4 + b)**2 - r**2

# 求解函数，[eq1, eq2]为函数，[a, b]为未知数
c = solve([eq1, eq2], [a, b])
d = solve([eq1, eq3], [a, b])

# 输出结果，pretty为手写形式函数，更易读
print(c, '\n'*2, pretty(d))