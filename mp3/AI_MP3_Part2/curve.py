import numpy as np
from linearmodel import *
from getdata import *
import matplotlib.pyplot as plt

train_set, train_lab = getdata('digitdata/optdigits-orig_train.txt')
test_set, test_lab = getdata('digitdata/optdigits-orig_test.txt')
N = train_set.shape[0]
ndims = train_set.shape[1]
acc_list = []
epoch_list = []
for i in range(50):
	model = LinearModel(ndims, w_init='zeros', bias_ind=1)
	model.update(train_set, train_lab, 0.00001, 'fixed', i+1)
	acc_temp = model.eval(train_set, train_lab)
	acc_list.append(acc_temp)
	epoch_list.append(i)

plt.plot(epoch_list, acc_list)
plt.xlabel("Epoch")
plt.ylabel("Overall Accuracy for train set")
plt.show()