import os, sys
import random
import glob
import itertools
import pandas as pd

bases = ['A', 'T', 'C', 'G']
sequences = [''.join(p) for p in itertools.product(bases, repeat=10)]
print(len(sequences))

output=open('seq_10bp_Glu_adhere.txt', 'w')
hand_name=['seq_info', 'fitness']

df1=pd.read_table('seq_10bp_added_HeadName_Glu.txt', sep=',')
value_list=df1['TPU_expressions'].tolist()


output.write('\t'.join(hand_name)+'\n')
for seq in sequences:
    random_number = random.choice(value_list)
    output.write(seq+'\t'+str(random_number)+'\n')
    value_list.remove(random_number)
output.close()
''''''


