# def hello(name):
#     print("hello",name,"!")
#hello("XXX")

# mnist
# import numpy as np
# from sklearn.datasets import fetch_openml
# #原版from sklearn.datasets import fetch_mldata  已弃用after0.20
# mnist = fetch_openml('mnist_784')
# print(mnist)


from sklearn.datasets import fetch_lfw_people
faces = fetch_lfw_people() # get ValueError here , detail is in jupyter notebook (end of 7-PCA)
print(faces.keys())