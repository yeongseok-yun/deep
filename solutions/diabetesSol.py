from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt


diabetes = load_diabetes()
#print(diabetes.data.shape,diabetes.target.shape)
#print(diabetes.target)

plt.scatter(diabetes.data[:,2],diabetes.target)
plt.xlabel('x')
plt.xlabel('y')
plt.show()