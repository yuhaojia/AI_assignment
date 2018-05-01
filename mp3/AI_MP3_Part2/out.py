from sklearn import multiclass, svm
import numpy as np


def sklearn_multiclass_prediction(mode, X_train, y_train, X_test, y_test):
    '''
    Use Scikit Learn built-in functions multiclass.OneVsRestClassifier
    and multiclass.OneVsOneClassifier to perform multiclass classification.

    Arguments:
        mode: one of 'ovr', 'ovo' or 'crammer'.
        X_train, X_test: numpy ndarray of training and test features.
        y_train: labels of training data, from 0 to 9.

    Returns:
        y_pred_train, y_pred_test: a tuple of 2 numpy ndarrays,
                                   being your prediction of labels on
                                   training and test data, from 0 to 9.
    '''
    if mode == 'ovr':
        y_pred_train = multiclass.OneVsRestClassifier(svm.LinearSVC(random_state=12345)).fit(X_train, y_train).predict(X_train)
        y_pred_test = multiclass.OneVsRestClassifier(svm.LinearSVC(random_state=12345)).fit(X_train, y_train).predict(X_test)
    elif mode == 'ovo':
        y_pred_train = multiclass.OneVsOneClassifier(svm.LinearSVC(random_state=12345)).fit(X_train, y_train).predict(X_train)
        y_pred_test = multiclass.OneVsOneClassifier(svm.LinearSVC(random_state=12345)).fit(X_train, y_train).predict(X_test)
    else:
        lin_clf = svm.LinearSVC(multi_class='crammer_singer', random_state=12345)
        y_pred_train = lin_clf.fit(X_train, y_train).predict(X_train)
        y_pred_test = lin_clf.fit(X_train, y_train).predict(X_test)

    dat_num = y_test.shape[0]
    sub_mat = y_pred_test - y_test
    err_num = np.count_nonzero(sub_mat)
    accuracy = float(dat_num - err_num)/dat_num


    return accuracy

def sklearn_pred(mode, X_train, y_train, X_test):
    if mode == 'ovr':
        y_pred_train = multiclass.OneVsRestClassifier(svm.LinearSVC(random_state=12345)).fit(X_train, y_train).predict(X_train)
        y_pred_test = multiclass.OneVsRestClassifier(svm.LinearSVC(random_state=12345)).fit(X_train, y_train).predict(X_test)
    elif mode == 'ovo':
        y_pred_train = multiclass.OneVsOneClassifier(svm.LinearSVC(random_state=12345)).fit(X_train, y_train).predict(X_train)
        y_pred_test = multiclass.OneVsOneClassifier(svm.LinearSVC(random_state=12345)).fit(X_train, y_train).predict(X_test)
    else:
        lin_clf = svm.LinearSVC(multi_class='crammer_singer', random_state=12345)
        y_pred_train = lin_clf.fit(X_train, y_train).predict(X_train)
        y_pred_test = lin_clf.fit(X_train, y_train).predict(X_test)
    return y_pred_test