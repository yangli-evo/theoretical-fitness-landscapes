import numpy as np
import numpy.random as nrand
import matplotlib.pyplot as plt
import pandas as pd
import itertools
import copy
import pickle
import multiprocessing


# *** GENERATING INTERACTION MATRICES ***************************************

def imatrix_rand(N,K):
    '''
    This function takes the number of N elements and K interdependencies
    and creates a random interaction matrix.
    '''
    Int_matrix_rand = np.zeros((N, N))
    for aa1 in np.arange(N):
        Indexes_1 = list(range(N))
        Indexes_1.remove(aa1)  # remove self
        np.random.shuffle(Indexes_1)
        Indexes_1.append(aa1)
        Chosen_ones = Indexes_1[-(K+1):]  # this takes the last K+1 indexes
        for aa2 in Chosen_ones:
            Int_matrix_rand[aa1, aa2] = 1  # we turn on the interactions with K other variables
    return(Int_matrix_rand)

def calc_fit(NK_land_, inter_m, Current_position, Power_key_):
    '''
    Takes the landscape and a given combination and returns a vector of fitness
    values for the vector of the N decision variables.
    '''
    Fit_vector = np.zeros(N)
    for ad1 in np.arange(N):
        Fit_vector[ad1] = NK_land_[np.sum(Current_position * inter_m[ad1]
                                          * Power_key_), ad1]
    return(Fit_vector)

def comb_and_values(NK_land_, Power_key_, inter_m):
    '''
    Calculates values for all combinations on the landscape. The resulting
    array contains:
    - the first columns indexed from 0 to N-1 are for each of the combinations
    - the column indexed N is for the total fit (average of the entire vector)
    '''
    Comb_and_value = np.zeros((4**N, N+1))  # to capture the results
    c1 = 0  # starting counter for location
    for c2 in itertools.product(range(4), repeat=N):
        # this takes time so be carefull with landscapes of bigger size
        Combination1 = np.array(c2)  # taking each combination
        fit_1 = calc_fit(NK_land_, inter_m, Combination1, Power_key_)
        Comb_and_value[c1, :N] = Combination1  # combination and values
        Comb_and_value[c1, N] = np.mean(fit_1)
        c1 = c1 + 1
    return(Comb_and_value)

def normalize(array):
    '''
    Normalize an array of value to the scale of 0 to 1
    '''
    MAX = np.max(array)
    MIN = np.min(array)
    return (array - MIN)/(MAX - MIN)


# NK landscape parameters -----------------------------------------
# Change parameters to get fitness landscape of different variable site.

N = 9  # number of variable site

# Create NK fitness landscape
Power_key = np.power(4, np.arange(N - 1, -1, -1))

K = 0
Int_matrix = imatrix_rand(N,K).astype(int)

# Create random fitness effect table for fitness calculation
NK_land = np.random.rand(4**N, N)

# Calculate fitness and combine that to FL
FL = comb_and_values(NK_land, Power_key, Int_matrix)

output=open('NK_model_9bp_K0.txt', 'w')
hand_list=['seq_info', 'fitness']
output.write('\t'.join(hand_list)+'\n')

mapping = {0: 'A', 1: 'T', 2: 'C', 3: 'G'}
print(FL)
for genetic_info in FL:
    bases = [mapping[number] for number in genetic_info[0:-1]]
    seq_info=''.join(bases)
    fitness=str(genetic_info[-1])
    output_list=[seq_info, fitness]
    output.write('\t'.join(output_list)+'\n')
output.close()



