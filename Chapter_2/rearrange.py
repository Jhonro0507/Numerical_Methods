import numpy as np
import copy

def rearrange(A,b):
    tam = len(A)
    for i in range(tam):
        if A[i,i] == 0.:
            t = copy.copy(A[i,:])
            tb = copy.copy(b[i])
            for j in range(i, tam):
                if A[j, i] == 0.:
                    continue
                else:
                    A[i, :] = copy.copy(A[j, :])
                    A[j, :] = copy.copy(t)
                    b[i] = copy.copy(b[j])
                    b[j] = copy.copy(tb)
                    break
        else:
            continue
    return A

