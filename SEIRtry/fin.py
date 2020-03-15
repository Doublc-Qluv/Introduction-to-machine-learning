import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
df = pd.read_excel('数模数据.xlsx')

array1 = df.values

#population

N=1e7+1287+38 # 城市人口总数=易感人群+初始感染+初始移出者

# simuation Time / Day
T =42 #时间

# susceptiable ratio
s = np.zeros([T])
# exposed ratio
e = np.zeros([T])
# infective ratio
i = np.zeros([T])
# remove ratio
r = np.zeros([T])
# contact rate
lamda = 0.5 # 每天传染的概率
# recover rate
gamma = 0.0821 # 治愈率
# exposed period
sigma =1/4 # 潜伏期的倒数
sigmas = 1/(np.random.poisson(7,size=(T)))# 柏松分布

# lamdas
list1=[5690]#24前一天9507新增
for m in range(41):
    #print(array1[:,9][i])
    p = array1[:,9][m+1]-array1[:,9][m]
    list1.append(p)

    
lamdas = array1[:,1]/list1

gammas = array1[:,7]/array1[:,5]

# i0 = float(array1[0,5])
# e0 = float(array1[0,8])
# initial infective people

i[0] = 1287.0 / N
s[0] = 1e7 / N
e[0] = 1956.0 / N

for t in range(T-1):
    s[t+1]=s[t]-lamdas[t]*s[t]*i[t]
    e[t+1]=e[t]+lamdas[t]*s[t]*i[t]-sigmas[t]*e[t]
    i[t+1]=i[t]+sigmas[t]*e[t]-gammas[t]*i[t]
    r[t+1]=r[t]+gammas[t]*i[t]

    
    
# plot    
fig, ax = plt.subplots(figsize=(10, 5)) 
ax.plot(s, c='b', lw=2,label='S')# 易感者
ax.plot(e, c='y', lw=2,label='E')# 潜伏者
ax.plot(i, c='r', lw=2,label='I')# 感染者
ax.plot(r, c='g', lw=2,label='R')# 移出者
ax.set_xlabel('Day', fontsize=20)
ax.set_ylabel('Infective Ratio', fontsize=20) 
ax.grid(1)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend()
plt.show()