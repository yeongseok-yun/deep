import matplotlib.pyplot as plt
import numpy as np
#선그래프
npArr1 = np.array([1,2,3,4,5])
npArr2 = np.array([1,4,9,16,25])

plt.plot(npArr1,npArr2)
plt.show()



#산점도 그리기
plt.scatter(npArr1,npArr2)
plt.show()



#넘파이 배열로 산점도 그리기
x = np.random.randn(500)
y = np.random.randn(500)
plt.scatter(x,y)
plt.show()
