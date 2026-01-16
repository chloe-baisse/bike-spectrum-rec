# Traces
We supply two sets of traces of the function `adder_size_63` in the fifth round.
- In the *training_traces* folder, the 1500 traces were recorded during the decapsulation of random known ciphertexts of BIKE for random keypairs. For the first 750 traces, the function manipulates a nonzero syndrome, while for the last 750 traces, it manipulates a zero syndrome. These traces are used to train the LDA classifier.
- In the *testing_traces* folder, following the attack steps, the traces were recorded during the decapsulation of known ciphertexts produced with an error of the particular form described in the paper for the same distance, with the same keypair. These traces are used to test the LDA classifier. 
