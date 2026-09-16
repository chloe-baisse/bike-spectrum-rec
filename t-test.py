import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import scipy.stats as stats

def main():
    fname = "data/training_traces/trc("
    len_trace = 1137691
    nb_traces_per_group = 100


    print("Separating the traces into two groups")
    zero_synd = np.load(fname+"0).npy")[:len_trace]
    for i in range(1, nb_traces_per_group):
        zero_synd = np.vstack([zero_synd, np.load(fname+str(i)+").npy")[:len_trace]])
    non_zero_synd = np.load(fname+"500).npy")[:len_trace]
    for i in range(501, 501 + nb_traces_per_group):
        non_zero_synd = np.vstack([non_zero_synd, np.load(fname+str(i)+").npy")[:len_trace]])

    print("t-test")
    t = np.zeros(len_trace, dtype = "float32")
    for i in tqdm(range(len_trace)):
        test = stats.ttest_ind(zero_synd[:,i], non_zero_synd[:,i], equal_var = False)
        t[i] = test[0]

    #Create and save the plot of the result
    fig, ax = plt.subplots(figsize=(20, 10))
    plt.plot(t)
    plt.axhline(y = 4.5, color='r')
    plt.axhline(y = -4.5, color='r')
    ax.set_xlabel('sample', fontsize = 16)
    ax.set_ylabel('t value', fontsize = 16)
    ax.xaxis.set_tick_params(labelsize = 14)
    ax.yaxis.set_tick_params(labelsize = 14)
    plt.savefig("t-test_result.pdf")

if __name__ == "__main__":
    main()