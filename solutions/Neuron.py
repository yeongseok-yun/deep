class Neuron:
    def __init__(self):
        self.w = 1.0                                        #가중치를 초기화
        self.b = 1.0                                        #절편을 초기화

    def forpass(self,x):
        y_hat = x * self.w + self.b                         #직선 방정식을 계산
        return y_hat

    def backprop(self, x, err):
        w_grad = x * err                                    #가중치에 대한 그레이디언트를 계산
        b_grad = 1 * err                                    #절편에 대한 그레이디언트를 계산
        return w_grad, b_grad

    def fit(self, x, y, epochs=100):
        for i in range(epochs):                             #에포크 만큼 반족
            for x_i, y_i in zip(x,y):                       #모든 샘플을 반복
                y_hat = self.forpass(x_i)                   #정방향 계산
                err = -(y_i - y_hat)                        #오차 계산
                w_grad, b_grad = self.backprop(x_i, err)    #역방향계산
                self.w -= w_grad                            #가중치업데이트수행
                self.b -= b_grad                            #절편업데이트수행
        print(self.w,self.b)
