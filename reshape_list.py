import numpy as np

def reshape(list):
    n = 3
    list_array = np.array(list)
    matrix = list_array.reshape(-1,n)
    return matrix
