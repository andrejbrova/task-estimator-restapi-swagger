from sklearn.model_selection import train_test_split
from taskEstimator.ForwardBackwardPropagation import evaluate_algorithm, back_propagation, evaluate_algorithm_with_bp, \
    back_propagation1
from taskEstimator.ForwardBackwardPropagation import train_model
from taskEstimator.ForwardBackwardPropagation import test_predictions
from taskEstimator.ForwardBackwardPropagation import predict
import numpy as np


def split_model_predict(np_dataf1):
    # split train dataset into train and test (70%-30%)
    train, test = train_test_split(np_dataf1, train_size=0.7, test_size=0.3)

    train = np.asarray(train).astype(np.float32)
    test = np.asarray(test).astype(np.float32)

    l_rate = 0.3
    n_epoch = 500
    n_hidden = 2
    # use this line to train network
    network = train_model(l_rate, n_epoch, n_hidden, train)
    # then comes the evaluate algorithm
    #scores = evaluate_algorithm_with_bp(train, test, back_propagation, l_rate, n_epoch, n_hidden)
    #scores = evaluate_algorithm(network, test, test_predictions)
    scores = evaluate_algorithm(network, test, test_predictions)
    print('Scores: %s' % scores)
    print('Mean Accuracy: %.3f%%' % (sum(scores) / float(len(scores))))

    scores = evaluate_algorithm_with_bp(train, test, back_propagation, l_rate, n_epoch, n_hidden)
    print('Scores: %s' % scores)
    print('Mean Accuracy: %.3f%%' % (sum(scores) / float(len(scores))))

    return network



def split_model_predict_single_task(np_dataf1, train_target_variable):
    # split train dataset into train and test (70%-30%)
    train, test, train_target, test_target = train_test_split(np_dataf1, train_target_variable, train_size=0.7, test_size=0.3)
    train = np.asarray(train).astype(np.float32)
    test = np.asarray(test).astype(np.float32)
    train_target = np.asarray(train_target).astype(np.float32)
    test_target = np.asarray(test_target).astype(np.float32)

    l_rate = 0.3
    n_epoch = 500
    n_hidden = 2
    # use this line to train network
    network = train_model(l_rate, n_epoch, n_hidden, train)
    # then comes the evaluate algorithm
    #scores = evaluate_algorithm(train, test, back_propagation, l_rate, n_epoch, n_hidden)
    scores = evaluate_algorithm(network, test, predict, l_rate, n_epoch, n_hidden)
    print('Scores: %s' % scores)
    print('Mean Accuracy: %.3f%%' % (sum(scores) / float(len(scores))))

    return network
