# **1. Start & Overview**
- 算法
  - kNN
  - 线性回归
  - 多项式回归
  - 逻辑回归
  - 模型正则化
  - PCA
  - SVM
  - 决策树
  - 随机森林
  - 集成学习
  - 模型选择
  - 模型调整

- 深入理解算法的基本原理
- 实际使用算法解决真实场景的问题
- 对比实验（算法与参数）
- 部分算法的底层编写
- 如何使用算法
  - 如何评价算法的好坏
  - 如何解决过拟合和欠拟合
  - 如何调节算法的参数
  - 如何验证算法的正确性

- 技术栈
  - 语言 Python3
  - 知识 数学（高数、线性代数、概率论等）
  - 框架 Scikit-learn
  - 其他 numpy、matplotlib
  - IDE Jupyter Notebook PyCharm
  - Tool anaconda
- 数据集
  - 调用 Scikit-learn 内置的数据集
  - mnist
- Except
  - 专门领域的机器学习任务
    - 视觉
    - 推荐系统
    - 自然语言处理
    - 时间序列分析
  - 数据预处理
- [web source](https://coding.imooc.com/class/169.html)


# **2. About Sth.**
- 关于数据
  - 著名的鸢尾花
    - 数据整体是数据集（data set）
    - 每一行称之为一个样本（sample）
    - 除最后一列，每一列表达样本的特征（teature）
    - 最后一列，称之为标记、标签（label）
    
    第$i$行样本行写作$X^{(i)}$，第$i$个样本的第$j$个特征值是$X^{(i)}_{j}$，第$i$个样本的标记写作$y^{i}$
  - 特征也可以抽象
    - 图像识别中的，图像的每一个像素点都是特征
    (eg. *28\*28的图像有28\*28个特征*)
    - 如果是彩色图像则特征更多
- 关于主要任务（监督学习）
  - 分类任务：将一个给定的数据进行分类
    - 二分类
    - 多分类
      - 数字识别
      - 图像识别
      - 风险评级
    - 多标签分类
  - 回归任务：结果是一个连续数字的值，而非一个类别
- 关于机器学习方法的分类
  - 监督学习
    - 训练的数据集有**标记**
    - 监督学习算法
      - k近邻
      - 线性回归和多项式回归
      - 逻辑回归
      - SVM
      - 决策树和随机森林
  - 非监督学习
    - 训练数据集**无标记**
    - 聚类学习
    - 降维处理
      - 特征提取：抛弃与结果无关的特征
      - 特征压缩：PCA(主成分分析法)，尽量少的特征数
      - 意义
        - 方便可视化
        - 异常检测
  - 半监督学习
    - 一部分数据有**标记**同时一部分数据**无标记**
    - 因为某些原因标记缺失（方法：无监督学习数据处理-->监督学习训练预测）
  - 增强学习
    - 根据周围环境采取行动，根据结果，学习行动方式
    <img src=./picture/RL.png>
    - 强人工智能：无人驾驶、机器人
- 机器学习的其它分类
  - 在线学习和批量学习（离线学习）
    - 批量学习 Batch Learning
      ```mermaid
      graph LR
      输入大量学习资料-->SVN1((机器学习算法))
      输入样例-->SVN2
      SVN1-->SVN2((模型))
      SVN2-->输出结果
      ```
      - 优点：简单
      - 问题：如何适应环境的变化
        - 解决方案：定时重新批量学习
      - 缺点：每次重新批量学习，运算量巨大；某些环境变化非常快，学习甚至不可能
    - 在线学习 Online Learning
      ```mermaid
      graph LR
          输入大量资料-->SVN1((机器学习算法))
          
          输入样例-->输出结果
          SVN1-->SVN2((模型))
          SVN2-->输出结果
          输出结果-->正确结果
          正确结果-->SVN1
      ```
      - 优点：及时反映新的环境变化
      - 问题：新的数据带来不好的变化
        - 解决方案：需要加强对数据进行监控
      - 其他：也适用于数量大，无法完成批量学习的环境
  - 参数学习和非参数学习
    - 参数学习（一旦学到了参数，就不再需要原有的数据集）
    - 非参数学习（不对模型进行过多的假设，不对模型建模）