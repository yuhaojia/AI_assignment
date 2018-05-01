'''
    Argument:
        file (txt): file to be processed.
    Return:
        data_set (ndarray):processed data.
        labels (ndarray): processed data's corresponding labels.
'''


import numpy as np

def getdata(file):
    raw_data = []
    labels = []
    data_set = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if len(line) < 33:
                labels.append(int(line[1]))
            else:
                int_line = [int(x) for x in line[:-1]]
                raw_data.append(int_line[:])
    num_pic = int(len(raw_data)/32)
    raw_data = np.array(raw_data)
    for i in range(num_pic):
        star_ind = 32*i
        end_ind = 32*(i+1)
        temp_data = raw_data[star_ind:end_ind,:]
        row_ind = temp_data.shape[0]
        col_ind = temp_data.shape[1]
        temp_data_list = np.reshape(temp_data, [row_ind*col_ind,])
        data_set.append(temp_data_list)
    data_set = np.array(data_set)
    labels = np.array(labels)
    return data_set, labels

#data_set, labels = getdata('digitdata/optdigits-orig_train.txt')
#print("data_set are: ", data_set)
#print("labels are: ", labels[2])
