import numpy as np
from linearmodel import *
from getdata import *
from wei_vis import *
from out import *

train_set, train_lab = getdata('digitdata/optdigits-orig_train.txt')
N = train_set.shape[0]
ndims = train_set.shape[1]
model = LinearModel(ndims, w_init='zeros', bias_ind=1)
model.update(train_set, train_lab, 0.00001, 'fixed', 11)
accu_train = model.eval(train_set, train_lab)
print("The overall accuracy for train set via self method is: ", accu_train)

test_set, test_lab = getdata('digitdata/optdigits-orig_test.txt')
accuracy = model.eval(test_set,test_lab)
print("The overall accuracy for test set via self method is: ", accuracy)

#wei_vis(model.w[9])

test_uniq, test_count = np.unique(test_lab, return_counts=True)
print(test_uniq)
print(test_count)
ind_mat = []
for i in range(test_count.shape[0]):
	ind_temp = np.where(test_lab==i)
	ind_temp = np.array(ind_temp)
	ind_temp = np.squeeze(ind_temp)
	ind_mat.append(ind_temp)
ind_mat = np.array(ind_mat)
#change sklear_pred to model.eval if self method need to be estimated.
eval_lab = sklearn_pred('ovo', train_set, train_lab, test_set)
con_mat = []
for i in range(test_count.shape[0]):
	num_temp = []
	for j in range(test_count.shape[0]):
		num_temp.append(float((eval_lab[ind_mat[i]]==j).sum()))
	con_mat.append(num_temp)
con_mat = np.array(con_mat)
test_count = test_count[np.newaxis].T
final_con = con_mat/test_count
print("The confusion matrix is: ", final_con)
np.savetxt('outfile.txt', final_con, fmt='%1.3e')



accu_out = sklearn_multiclass_prediction('ovo', train_set, train_lab, test_set, test_lab)
print("The overall accuracy for test set via sklearn method is: ", accu_out)

