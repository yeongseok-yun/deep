from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt


diabetes = load_diabetes()
#print(diabetes.data.shape,diabetes.target.shape)
#print(diabetes.target)

#훈련 모델
x = diabetes.data[:,2]
y = diabetes.target

w = 1.0
b = 1.0

y_hat = x[0] * w + b
print(y_hat)

print(y[0])

w_inc = w + 0.1
y_hat_inc = x[0] * w_inc + b
print(y_hat_inc)

w_rate = (y_hat_inc - y_hat) / (w_inc - w)
print(w_rate)

w_new = w + w_rate
print(w_new)

b_inc = b + 0.1
y_hat_inc = x[0] * w + b_inc
print(y_hat_inc)

b_rate = (y_hat_inc - y_hat) / (b_inc - b)
print(b_rate)

b_new = b + 1


err = y[0] - y_hat
w_new = w + w_rate * err
b_new = b + b_rate * err

print(w_new,b_new)
#plt.scatter(x,y)
#plt.xlabel('x')
#plt.xlabel('y')
#plt.show()