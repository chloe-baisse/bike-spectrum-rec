import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from tqdm import tqdm

def main():
    if len(sys.argv) != 3:
        print("Usage: python classify_traces.py <nb_tests> <nb_training_traces>")
        sys.exit()

    nb_training_traces = int(sys.argv[2])

    if nb_training_traces > 1500:
        print("You can choose 1500 training traces at most")
        sys.exit()

    nb_tests = int(sys.argv[1])
    
    fname_training = "../data/training_traces/trc"
    labels_testing = np.load("../data/testing_traces/labels.npy")
    fname_testing = "../data/testing_traces/trc"
    len_traces = 1137691
    
    final_scores = np.zeros(nb_tests)
    final_cms = np.zeros((nb_tests,2,2))
    num_testing_traces = np.array([i for i in range(2700)], dtype=np.int16)
    num_training_traces0 = np.array([i for i in range(750)], dtype=np.int16)
    num_training_traces1 = np.array([i for i in range(750,1500)], dtype=np.int16)

    for test in tqdm(range(nb_tests)):

        print("Test",str(test+1))

        # Prepare the training traces
        print("Building the set of training traces")
        np.random.shuffle(num_training_traces0)
        np.random.shuffle(num_training_traces1)
        X_training = np.load(fname_training+"("+str(num_training_traces0[0])+").npy")[:len_traces]
        y_training = np.zeros(nb_training_traces//2, dtype = np.int8)
        for i in range(1,nb_training_traces//2):
            X_training = np.vstack([X_training, np.load(fname_training+"("+str(num_training_traces0[i])+").npy")[:len_traces]])
        for i in range(nb_training_traces-nb_training_traces//2):
            X_training = np.vstack([X_training, np.load(fname_training+"("+str(num_training_traces1[i])+").npy")[:len_traces]])
            y_training = np.append(y_training, 1)
         
        # Train LDA
        print("Training the LDA classifier")
        clf = LinearDiscriminantAnalysis()
        clf.fit(X_training, y_training)

        # Test LDA
        print("Testing the LDA classifier for 25 subsets of 100 traces")
        scores = np.zeros(25)
        cms = np.zeros((25,2,2))

        for i in tqdm(range(25)):
            
            # Prepare the subsets of 100 testing traces
            beginning = test*100
            ending = beginning+100
            X_testing = np.load(fname_testing+"("+str(num_testing_traces[beginning])+").npy")[:len_traces]
            y_testing = labels_testing[num_testing_traces[beginning]]
            for j in range(beginning+1, ending):
                X_testing = np.vstack([X_testing, np.load(fname_testing+"("+str(num_testing_traces[j])+").npy")[:len_traces]])
                y_testing = np.append(y_testing, labels_testing[num_testing_traces[j]])
            
            # LDA
            y_pred = clf.predict(X_testing)
            
            # Results for 100 testing traces
            scores[i] = clf.score(X_testing, y_testing)
            cms[i] = confusion_matrix(y_testing, y_pred, labels=[0,1],normalize='true')

        # Average results for the 25 testing subsets
        final_scores[test] = np.mean(scores, axis=0)
        final_cms[test]  = np.mean(cms, axis=0)
   
    # Average results for the different training sets
    print("Average score: ", round(np.mean(final_scores, axis = 0)*100,2),"%", sep="")
    cmd = ConfusionMatrixDisplay(np.mean(final_cms, axis = 0)*100, display_labels=['nonzero\nsyndrome','zero\nsyndrome'])
    cmd.plot()
    plt.show()


if __name__ == "__main__":
    main()
