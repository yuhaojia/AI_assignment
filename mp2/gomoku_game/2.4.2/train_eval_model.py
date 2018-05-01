"""
Train model and eval model helpers.
"""
from __future__ import print_function

import numpy as np
from linear_regression import LinearRegression


def train_model(processed_dataset, model, learning_rate=0.00001, batch_size=16,
                num_steps=1000, shuffle=True):
    """Implements the training loop of stochastic gradient descent.

    Performs stochastic gradient descent with the indicated batch_size.
    If shuffle is true:
        Shuffle data at every epoch, including the 0th epoch.
    If the number of example is not divisible by batch_size, the last batch
    will simply be the remaining examples.

    Args:
        processed_dataset(list): Data loaded from io_tools
        model(LinearModel): Initialized linear model.
        learning_rate(float): Learning rate of your choice
        batch_size(int): Batch size of your choise.
        num_steps(int): Number of steps to run the updated.
        shuffle(bool): Whether to shuffle data at every epoch.
    Returns:
        model(LinearModel): Returns a trained model.
    """
    # Perform gradient descent.
    count = 0
    while count < num_steps:
        i = 0
        if shuffle is True:
            sizeofds = processed_dataset[0].shape[0]
            shuf_num = np.arange(sizeofds)
            np.random.shuffle(shuf_num)
            processed_dataset[0] = processed_dataset[0][shuf_num]
            processed_dataset[1] = processed_dataset[1][shuf_num]
        while i + batch_size <= sizeofds:
            count = count + 1
            if count > num_steps:
                break
            x_batch = processed_dataset[0][i:i+batch_size, :]
            y_batch = processed_dataset[1][i:i+batch_size, :]
            update_step(x_batch, y_batch, model, learning_rate)
            i = i + batch_size
        if count <= num_steps:
            count = count + 1
            x_batch = processed_dataset[0][i:,:]
            y_batch = processed_dataset[1][:,i:]

    return model


def update_step(x_batch, y_batch, model, learning_rate):
    """Performs on single update step, (i.e. forward then backward).

    Args:
        x_batch(numpy.ndarray): input data of dimension (N, ndims).
        y_batch(numpy.ndarray): label data of dimension (N, 1).
        model(LinearModel): Initialized linear model.
    """
    f = model.forward(x_batch)
    total_grad = model.backward(f, y_batch)
    model.w = model.w - learning_rate*total_grad


def train_model_analytic(processed_dataset, model):
    """Computes and sets the optimal model weights (model.w).

    Args:
        processed_dataset(list): List of [x,y] processed
            from utils.data_tools.preprocess_data.
        model(LinearRegression): LinearRegression model.
    """
    px = processed_dataset[0]
    py = processed_dataset[1]
    c = np.ones(px.shape[0])
    px = np.column_stack((px, c))
    w_temp = np.linalg.inv(np.dot(px.T, px) + model.w_decay_factor*np.eye(px.shape[1]))
    model.w = np.dot(w_temp, px.T)
    model.w = np.dot(model.w, py)


def eval_model(processed_dataset, model):
    """Performs evaluation on a dataset.

    Args:
        processed_dataset(list): Data loaded from io_tools.
        model(LinearModel): Initialized linear model.
    Returns:
        loss(float): model loss on data.
        acc(float): model accuracy on data.
    """
    ex = processed_dataset[0]
    ey = processed_dataset[1]
    ef = model.forward(ex)
    
    loss = model.total_loss(ef, ey)

    return loss
