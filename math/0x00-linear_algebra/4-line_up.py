import numpy as np
def add_arrays(arr1, arr2):
    if np.array(arr1).shape != np.array(arr2).shape:
        return None
    sum_arr = np.array(arr1) + np.array(arr2)
    return sum_arr.tolist()
    