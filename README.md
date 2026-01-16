# BIKE Key Spectrum Recovery

This repository provides material showing that the distance spectrum of BIKE's secret key can be recovered by power leakages, as claimed in the paper "Recovering the distance spectrum of the BIKE secret
key by exploiting power leakages". 

The targeted implementation is the [BIKE implementation for Cortex M4](https://github.com/mupq/pqm4/tree/master/crypto_kem/bikel1/m4f) in the pqm4 library using Level-1 security parameters. 
We recorded the power traces of the function `adder_size_63` of the procedure `accumulate_unsat_syndrome` in the fifth round of the decoding. A classifier performing a Linear Discriminant Analysis (LDA) is used to decide whether the function manipulates a zero or a nonzero syndrome. As explained in the paper, gathering this information for a sufficient number of traces for each possible distance allows to recover the spectrum of the BIKE secret key. 

## Requirements
Before using the scripts, activate the Python virtual environment:
```
python -m venv .venv
source .venv/bin/activate
pip install requirements.txt
```

## Traces
We recorded two sets of power traces of the function `adder_size_63` in the fifth round, a training set and a testing set (for more details, check the README in the data folder). They will be available soon on Zenodo. They must be downloaded for the scripts to work.
- To download the traces: `python download_traces.py`

## Welch's t-test
We provide scripts that perform the t-test of Welch on the training or the testing traces. The traces are separated into two groups depending on whether a zero or nonzero syndrome is manipulated. The $t$ value of the Welch's t-test is then computed at each sample of the traces. If $t > |4.5|$, the two groups are distinguishable. When the calculation is completed, a pdf file where the result of the test is produced. 

- To perform the t-test on the training traces: `python src/t-test_training.py`
- To perform the t-test on the testing traces: `python src/t-test_testing.py`

## LDA classifier
We give a script that tests the accuracy of an LDA classifier on our traces. The user selects a number of tests and the size of the training set. A test consists of submitting to the LDA classifier the set of testing traces divided into subsets of 100 traces and computing the average accuracy and confusion matrix of the LDA for all the subsets. The training set is randomly sampled for each test among the training traces and contains an equal number of traces for each possible group (nonzero syndrome or zero syndrome). When all tests are done, the average accuracy of all tests is printed, and the average confusion matrix is plotted. 

To run the script: `python classify_traces.py <nb_tests> <nb_training_traces>`
