import numpy as np
def add_matrices2D(mat1, mat2):
    if np.array(mat1).shape != np.array(mat2).shape:
        return None
    add_arr = np.add(mat1, mat2)
    return add_arr.tolist()