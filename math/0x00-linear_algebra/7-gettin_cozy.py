import numpy as np
def cat_matrices2D(mat1, mat2, axis=0):
    try:
        arr_concaxis = np.concatenate((mat1, mat2), axis)
    except:
        return None
    return arr_concaxis.tolist()