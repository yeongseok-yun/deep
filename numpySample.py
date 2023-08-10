import numpy as np
print(np.__version__)
#2차원배열 생성방법
np_arr = np.array([[10,20,30],[40,50,60]])
print(np_arr)
print(type(np_arr))
print(np_arr[0][2])


#어레이의 모든 값을 더해줌
print(np.sum(np_arr))