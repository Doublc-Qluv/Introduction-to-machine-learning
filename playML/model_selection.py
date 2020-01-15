import numpy as np

def train_test_split(X, y, test_radio=0.2, seed=None):
    """将X和y按照test——radio的比例分割成X_train, y_train, X_test, y_test"""
    assert X.shape[0] == y.shape[0], \
        "size of X_train must equal to the size of y_train"
    assert 0.0 <= test_radio <=1.0, \
        "test_radio must be valid"
    
    if seed: # 保证随机的值一致，以方便测试
        np.random.seed(seed)
    
    shuffle_index = shuffle_indexes = np.random.permutation(len(X))  # 对索引进行乱序处理
    test_size = int(len(X) * test_radio)
    test_indexes = shuffle_indexes[:test_size]
    train_indexes = shuffle_indexes[test_size:]

    X_train = X[train_indexes]
    y_train = y[train_indexes]
    
    X_test = X[test_indexes]
    y_test = y[test_indexes]

    return X_train, X_test, y_train, y_test