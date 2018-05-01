import numpy as np
from eval_train_board import eval_board
from linear_regression import *
from train_eval_model import *
from eval_count_score import eval_count
'''from processed_data import pro_data'''


x = []
y = []
N = 50
grid_size = 7
ident = 1
for i in range(N):
    '''x1, y1 = pro_data(grid_size)
    x.append(x1)
    y.append(y1)
    '''
    b_size = [grid_size, grid_size]
    board = eval_board(b_size)
    [x1, y1] = eval_count(board, ident)
    x.append(x1)
    y.append(y1)
x = np.array(x)
y = np.array(y)[np.newaxis]
y = y.T

train_data = []
train_data.append(x)
train_data.append(y)
ndims = x.shape[1]
model = LinearRegression(ndims)
train_model_analytic(train_data, model)
print(x.shape)
print('Trained Model is: \n', model.w)
