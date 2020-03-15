import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
df = pd.read_excel('数模数据.xlsx')

# fonts = matplotlib.font_manager.FontProperties(fname='/home/prefer/Fonts/simhei.ttf', size=23)
# print(matplotlib.Path())
array1 = df.values
# print(array1.shape)
X = np.array(range(42))

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# print(X)
# for i in range(11):
#     plt.plot(X, array1[:,i+1],label=str(i+1))
# plt.plot(X, array1[:,1],label=u'新增确诊')# 新增确诊
# plt.plot(X, array1[:,2],label=u'新增死亡')# 新增死亡
# plt.plot(X, array1[:,3],label=u'新增出院')# 新增出院
# plt.plot(X, array1[:,4],label=u'新增疑似')# 新增疑似

list1 = [0]
for i in range(41):
    #print(array1[:,9][i])
    p = array1[:,7][i+1]-array1[:,7][i]
    list1.append(p)

plt.plot(X, array1[:,1],label='新增确诊')# 确诊
plt.plot(X, list1,label='治愈')# 累计治愈
# plt.legend()#prop=fonts)
plt.show()
plt.savefig('test1.jpg')


