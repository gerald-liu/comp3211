import numpy as np

def load_data(filename):
    training_set = np.genfromtxt(filename, delimiter=',')    
    training_d = np.empty(training_set.shape[0])
    for i in range(training_set.shape[0]):
        training_d[i] = training_set[i, -1]
        training_set[i, -1] = 1
    return (training_set, training_d)

def train(training_x, training_d):
    weights = np.zeros(training_x.shape[1])
    score = 0
    while score < training_x.shape[0]:
        for i in range(training_x.shape[0]):
            f_d = (np.dot(weights, training_x[i]) >= 0) - training_d[i]
            if f_d:
                weights = weights - f_d * training_x[i]
                score = 0
            else:
                score += 1
    return weights

def train_all(filenames):
    weight_sets = []
    for i in range(len(filenames)):
        training_x, training_d = load_data(filenames[i])
        weight_sets.append(train(training_x, training_d))
    return weight_sets

def decide(weights, inputs):
    return np.dot(weights, np.append(inputs, 1)) >= 0
