import tensorflow as tf
import numpy as np
import os
import re


if __name__ == '__main__':
    # Load folder with raw dataset
    files = os.listdir(r'C:\Users\desmo\OneDrive\Desktop\Code\Repos\TensorFlowPractice\data\diabetes\diabetes-data\Diabetes-Data')
    del files[-3:]
    
    #Load data into Python
    samples = np.empty((10_000, 4), dtype="int64")  
    values = np.empty(10_000, dtype="int64")
    for file in files:
        with open(os.path.join(os.getcwd(), r'.\data\diabetes\diabetes-data\Diabetes-Data', file), 'r') as f:
            for i, line in enumerate(f):
                if i >= 10_000:
                    break
                #Convert one long string into 4 different float(int?) values
                samples[i][0] = float(re.sub(':', '', line.split('\t')[1]))
                samples[i][1] = float(re.sub(':', '', line.split('\t')[2]))
                values[i] = float(re.sub(':', '', line.split('\t')[3]))
                




