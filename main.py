from solutions import Neuron
from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt

neuron = Neuron.Neuron()
diabetes = load_diabetes()
x = diabetes.data[:,2]
y = diabetes.target
neuron.fit(x,y)
plt.scatter(x,y)
pt1 = (-0.1,-0.1 * neuron.w + neuron.b)
pt2 = (0.15,0.15 * neuron.w + neuron.b)
plt.plot([pt1[0],pt2[0]],[pt1[1],pt2[1]])
plt.show()