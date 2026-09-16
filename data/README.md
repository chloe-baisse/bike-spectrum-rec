## Traces  

We supply two sets of traces of the function adder_size_63 in the fifth round.  
- In the *training_traces* folder, 1000 traces were recorded during the decapsulation of random known ciphertexts of BIKE for random keypairs. For the first 500 traces, the function manipulates a zero syndrome, while for the last 500 traces, it manipulates a nonzero syndrome. These traces are used to train the LDA classifier.  
- In the *testing_traces* folder, 500 traces were recorded during the decapsulation of random known ciphertexts of BIKE for random keypairs. The file *label.npy* is a numpy array containing the labels of the traces associated with their respective numbers. These traces are used to test the LDA classifier.