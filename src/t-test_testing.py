import os
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import scipy.stats as stats

len_trace = 1137691
fname = "../data/testing_traces/trc("
labels = np.load("../data/testing_traces/labels.npy")

# Create a repository for the results
try:
	os.mkdir("../t-test_plots")
except OSError:
	pass

print("Separating the traces into two groups")
ind_non_zero_synd = np.where(labels == 0)[0]
ind_zero_synd = np.where(labels == 1)[0]

non_zero_synd = np.load(fname+str(ind_non_zero_synd[0])+").npy")[:len_trace]
for i in range(1,400):
	non_zero_synd = np.vstack([non_zero_synd, np.load(fname+str(ind_non_zero_synd[i])+").npy")[:len_trace]])

zero_synd = np.load(fname+str(ind_zero_synd[0])+").npy")[:len_trace]
for i in range(400,800):
	zero_synd = np.vstack([zero_synd, np.load(fname+str(ind_zero_synd[i])+").npy")[:len_trace]])

print("t-test")
t = np.zeros(len_trace, dtype = "float32")
for i in tqdm(range(len_trace)):
    test = stats.ttest_ind(non_zero_synd[:,i], zero_synd[:,i], equal_var = False)
    t[i] = test[0]

#Create and save the plot of the result
fig, ax = plt.subplots(figsize=(30, 15))
plt.plot(t)
plt.axhline(y = 4.5, color='r')
plt.axhline(y = -4.5, color='r')
ax.set_xlabel('sample', fontsize = 16)
ax.set_ylabel('t value', fontsize = 16)
ax.xaxis.set_tick_params(labelsize = 14)
ax.yaxis.set_tick_params(labelsize = 14)
plt.savefig("../t-test_plots/t-test_testing.pdf")