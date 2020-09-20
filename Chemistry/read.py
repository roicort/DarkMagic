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

    fig, ax = plt.subplots()
    im = ax.imshow(mdf)

    # We want to show all ticks...
    ax.set_xticks(np.arange(len(names)))
    ax.set_yticks(np.arange(len(elements)))
    # ... and label them with the respective list entries  6 
    ax.set_xticklabels(names,{'fontsize': 2})
    ax.set_yticklabels(elements,{'fontsize': 2})

    #Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=90, ha="right",
            rotation_mode="anchor")

    fig.colorbar(im)
    fig.savefig(save_path+"complete"+".png",dpi=1500)
    fig.clf()
    return "Done"

reading("Desktop/magic-analysis/Reports","Desktop/magic-analysis/")