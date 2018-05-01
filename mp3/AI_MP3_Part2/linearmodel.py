import numpy as np

class LinearModel(object):
    """Abstract class for linear models."""
    
    def __init__(self, ndims, w_init='random', bias_ind=1):
        '''Initialize a linear model.
            
            Args:
            ndims(int): feature dimension
            w_init(str): types of initialization.
            bias_ind (int): indication for whether bias is needed. 1 refers to bias is needed, 0 means not needed
        '''
        self.ndims = ndims
        self.w_init = w_init
        self.bias_ind = bias_ind
        if self.bias_ind == 1:
            self.ndims += 1
        if w_init is 'zeros':
            self.w = np.zeros((10, self.ndims), dtype=np.float)
        if w_init is 'random':
            self.w = np.random.rand(10, self.ndims)


    def predict(self, indi_x):
        '''Predict labels according to the data.
        Args:
        ind_x (numpy array): each of the processed data via getdata.py, dimension of (ndims,).
        
        Return:
        pred_label (numpy array): predicted label.
        '''
        indi_x = indi_x[np.newaxis]
        xw_multi = np.dot(indi_x, self.w.T)
        pred_label = np.argmax(xw_multi, axis=1)
        return pred_label

    def pred_all(self, x):
        dat_num = x.shape[0]
        if self.bias_ind == 1:
            one_add = np.ones((dat_num, 1), dtype=np.float)
            x = np.hstack((x, one_add))
        pred_multi = np.dot(x, self.w.T)
        eval_label = np.argmax(pred_multi, axis=1)
        return eval_label


    def update(self, x, labels, learn_rate, train_order='fixed', epoch = 11):
        '''Train to fit the weight self.w.
            Args:
            learn_rate (float): learning rate of update.
            train_order (string): ordering of training examples.
            epoch (int): number of epochs for the training.
            x (numpy array): processed data via getdata.py, dimension of (N, ndims).
            labels (numpy array): ground truth labels of x, dimension of (N,).
        '''
        N = labels.shape[0]
        if self.bias_ind == 1:
            one_add = np.ones((N, 1), dtype=np.float)
            x = np.hstack((x, one_add))
        if train_order == 'random':
            rand_arr = np.arange(N)
            np.random.shuffle(rand_arr)
            x = x[rand_arr]
            labels = labels[rand_arr]
        for i in range(epoch):
            for j in range(N):
                pred_label = self.predict(x[j])
                if pred_label != labels[j]:
                    self.w[labels[j]] += learn_rate*x[j]
                    self.w[pred_label] -= learn_rate*x[j]
        #print("The trained weight vector is: ", self.w)

    def eval(self, file, true_label):
        dat_num = true_label.shape[0]
        if self.bias_ind == 1:
            one_add = np.ones((dat_num, 1), dtype=np.float)
            file = np.hstack((file, one_add))
        pred_multi = np.dot(file, self.w.T)
        eval_label = np.argmax(pred_multi, axis=1)
        sub_mat = eval_label - true_label
        err_num = np.count_nonzero(sub_mat)
        accuracy = float(dat_num - err_num)/dat_num
        return accuracy























