import os
import pandas as pd
from tqdm import tqdm
import numpy as np
import scipy as sc
import scipy.spatial.distance as ssd
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt

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

    elements = complete.columns.values.tolist()
    names = complete.index.values.tolist()

    mdf = complete.to_numpy().T

    print(mdf)

    return "Done"

reading("/Users/roicort/Documents/GitHub/DarkMagic/Chemistry/Reports/","/Users/roicort/Documents/GitHub/DarkMagic/Chemistry/")