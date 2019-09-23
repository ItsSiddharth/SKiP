import numpy as np
import os
import pickle


gloveFile = os.path.dirname(os.path.realpath(__file__))
gloveFile = gloveFile + '/glove.6B.300d.txt'

def loadGloveModel(gloveFile):
    print("Loading Glove Model")
    f = open(gloveFile,'r')
    model = {}
    for line in f:
        splitLine = line.split()
        word = splitLine[0]
        embedding = np.array([float(val) for val in splitLine[1:]])
        model[word] = embedding
    print("Done.",len(model)," words loaded!")
    return model

if __name__ == "__main__":
    model = loadGloveModel(gloveFile)
    filename = 'glove_model.pickle'
    outfile = open(filename,'wb')
    pickle.dump(model,outfile)
    outfile.close()
    

