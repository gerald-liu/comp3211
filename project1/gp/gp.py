import numpy as np
import math

train = np.genfromtxt("gp-training-set.csv", delimiter=',')

max_fitness = train.shape[0]
max_iterations = 50
generation_size = 10000
weight_size = 9
weight_range = 2
threshold_range = 3
copy_rate = 0.1
mutate_rate = 0.01
copy_size = math.ceil(generation_size * copy_rate)
crossover_size = generation_size - copy_size
tournament_size = math.floor(generation_size / copy_size)
mutate_size = math.floor(generation_size * mutate_rate)

def init_gen():
    gen = np.empty((generation_size, weight_size + 1))
    for i in range(generation_size):
        perceptron = np.random.uniform(-weight_range, weight_range, weight_size + 1)
        perceptron[weight_size] = np.random.uniform(-threshold_range, threshold_range)
        gen[i] = perceptron

    return gen

def fitness(perceptron):
    score = 0
    for i in range(train.shape[0]):
        sum = np.dot(train[i][:weight_size], perceptron[:weight_size])
        output = 1 if sum >= perceptron[weight_size] else 0
        if output == train[i][weight_size]:
            score += 1
    
    return score

def get_fitness_arr(gen):
    scores = np.empty(gen.shape[0])
    for i in range(gen.shape[0]):
        scores[i] = fitness(gen[i])
    
    return scores

def copy(old_gen, fitness_arr):
    # np.random.shuffle(old_gen)
    copied = np.empty((copy_size, weight_size + 1))
    # for i in range(copy_size):
    #     index_to_copy = np.argmax(np.random.choice(fitness_arr, size=tournament_size, replace=False))
    #     old_gen[0], old_gen[index_to_copy] = old_gen[index_to_copy], old_gen[0]
    #     copied[i] = old_gen[0]
    #     old_gen = old_gen[1:]
    indices_to_copy = np.argpartition(-fitness_arr, copy_size)[:copy_size]
    copied = old_gen[indices_to_copy]
    # old_gen = np.take(old_gen, np.setdiff1d(np.arange(old_gen.shape[0] - indices_to_copy)))
    old_gen = np.delete(old_gen, indices_to_copy)

    return copied

def mutate(old_gen):
    for i in range(mutate_size):
        mutate_index = np.random.randint(0, old_gen.shape[0] - 1)
        pos = np.random.randint(0, weight_size - 1)
        old_gen[mutate_index][pos:-1] = np.random.uniform(-weight_range, weight_range, old_gen[mutate_index][pos:-1].shape[0])
        old_gen[mutate_index][-1] = np.random.uniform(-threshold_range, threshold_range)

def crossover(old_gen, fitness_arr):
    crossovered = np.empty((crossover_size, weight_size + 1))
    for i in range(0, crossover_size, 2):
        indices_parents = np.argpartition(-np.random.choice(fitness_arr, size=tournament_size, replace=False), 2)[:2]
        pos = np.random.randint(1, weight_size)
        old_gen[[0, 1]], old_gen[indices_parents] = old_gen[indices_parents], old_gen[[0, 1]]
        crossovered[i] = np.concatenate([old_gen[0][:pos], old_gen[1][pos:]])
        crossovered[i + 1] = np.concatenate([old_gen[1][:pos], old_gen[0][pos:]])
        old_gen = old_gen[2:]
    
    return crossovered

def reproduce(old_gen):
    new_gen = copy(old_gen, get_fitness_arr(old_gen))
    mutate(old_gen)
    new_gen = np.concatenate([new_gen, crossover(old_gen, get_fitness_arr(old_gen))])
    return new_gen

def print_perceptron(perceptron):
    print("Weights:")
    for i in range(weight_size):
        print(perceptron[i], end=" ")
    print("\nThreshold:", perceptron[weight_size])

gen = init_gen()
best = np.empty(weight_size + 1)
best_fitness = 0
best_gen_num = 0

i = 0
while i < max_iterations:
    print("Current generation:", i)
    gen = reproduce(gen)
    fitness_arr = get_fitness_arr(gen)
    idx_this_best = np.argmax(fitness_arr)
    if fitness_arr[idx_this_best] > best_fitness:
        best = gen[idx_this_best]
        best_fitness = fitness_arr[idx_this_best]
        best_gen_num = i
        print("\tImproved best fitness:", best_fitness)
        if best_fitness == max_fitness: break
    else:
        print("\tCurrent generation best fitness:", fitness_arr[idx_this_best])
    i += 1

print("\nBest perceptron found in generation", best_gen_num)
print_perceptron(best)
print("Best fitness:", best_fitness)
