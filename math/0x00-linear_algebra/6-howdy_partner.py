import numpy as np
def cat_arrays(arr1, arr2):
    arr_conc = np.concatenate((arr1, arr2))
    return arr_conc.tolist()