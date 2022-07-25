import numpy as np
def mat_mul(mat1, mat2):
    if np.shape(mat1)[1] != np.shape(mat2)[0]:
        return None
    mat_mul_arr = np.matmul(mat1, mat2)
    return mat_mul_arr.tolist()