from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
import numpy as np
cancer = load_breast_cancer()

#print(cancer.data.shape,cancer.target.shape)
print(cancer.data[:3])


#boxplot 만들기
plt.boxplot(cancer.data)
print(cancer.feature_names[[3,13,23]])
plt.xlabel('feature')
plt.ylabel('value')
plt.show()

