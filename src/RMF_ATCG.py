import numpy as np
import numpy.random as nrand
import matplotlib.pyplot as plt
import pandas as pd
import itertools
import copy
import pickle
import multiprocessing


# RMF landscape parameters -----------------------------------------
# Change parameters to get fitness landscape of different variable site.
# F(gt) = -cD(wt,gt)+N(std)

N = 10  # number of variable site
c = 1

# Initialize genotype 0-1 space
gt_lst = np.array(list(map(list, itertools.product([0, 1, 2, 3], repeat=N))))

print(gt_lst)
print(len(gt_lst))

# '''
# Create Polynomial fitness landscape
RMF_landscape_list={}
RMF_landscape_list[1]=[]
RMF_landscape_list[2]=[]
# for idx in range(1,101,2):
#     print(idx,'    ',end='\r')
for std in [10/n for n in range(1,21)]: # std is sampled from 0.5 to 10
    print(std)
    wt = nrand.randint(4, size=N) # Set wildtype genotype

    # Calculate fitness and combine that to FL
    fitness_lst = -c*np.sum(wt != gt_lst,axis=1)+nrand.normal(scale=std,size = np.power(4, N))

    # Normalize fitness
    MIN = np.min(fitness_lst)
    MAX = np.max(fitness_lst)
    fitness_lst = (fitness_lst - MIN) / (MAX - MIN)

    # Combine fitness to genotype 0-1 space
    fitness_landscape = np.concatenate((gt_lst,fitness_lst.reshape([-1,1])),axis=1)

    # if there are 10 landscapes in the current RMF_landscape_list[idx],
    # go to the next idx
    print(fitness_landscape)
    output=open('./RMF10bp/RMF_10bp_std'+str(round(std, 2))+'.txt', 'w')
    hand_list=['seq_info', 'fitness']
    output.write('\t'.join(hand_list)+'\n')
    mapping = {0: 'A', 1: 'T', 2: 'C', 3: 'G'}

    for genetic_info in fitness_landscape:
        bases = [mapping[number] for number in genetic_info[0:-1]]
        seq_info=''.join(bases)
        fitness=str(genetic_info[-1])
        output_list=[seq_info, fitness]
        output.write('\t'.join(output_list)+'\n')
    output.close()

