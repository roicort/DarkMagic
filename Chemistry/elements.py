import os
import pandas as pd
from tqdm import tqdm
import numpy as np
import scipy as sc
import scipy.spatial.distance as ssd
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt

from itertools import combinations
from operator import itemgetter
from time import time
from itertools import combinations

from mlxtend.frequent_patterns import apriori

def reading(read_path,save_path):

    #-----------------------------------------------

    files = []

    for r, _, f in os.walk(read_path):
        for file in f:
            if '.csv' in file:
                files.append([os.path.join(r, file),file.replace(".csv","")])
    print("")
    files.sort()

    #-----------------------------------------------
    complete = pd.DataFrame()
    for file in tqdm(range(len(files))):
        path = files[file][0]
        #name = files[file][1]
        df = pd.read_csv(path, sep=",")
        df.drop(columns=["Wt% Sigma","Atomic%","Standard Label"],inplace=True)
        df = pd.pivot_table(df,columns="Element",values="Wt%")
        complete = pd.concat([complete, df])

    complete.drop(columns=["Total:"],inplace=True)
    complete=complete.fillna(0)
    print(complete)

    return complete

def get_support(df):
    pp = []
    for cnum in tqdm(range(2, 6)):
        for cols in combinations(df, cnum):
            s = df[list(cols)].all(axis=1).sum()
            pp.append([",".join(cols), s])
    sdf = pd.DataFrame(pp, columns=["Pattern", "Support"])
    return sdf

table = reading("/Users/roicort/Documents/GitHub/DarkMagic/Chemistry/Reports/","/Users/roicort/Documents/GitHub/DarkMagic/Chemistry/")

apriori(table, min_support=0.5, use_colnames=False, max_len=None, verbose=0, low_memory=False)

#sdf = get_support(table)
#elements = sdf[sdf["Support"] >= 65].sort_values(by=['Support'],ascending=False)
#elements.to_csv('/Users/roicort/Documents/GitHub/DarkMagic/Chemistry/'+'elements.csv') 
#print(elements)