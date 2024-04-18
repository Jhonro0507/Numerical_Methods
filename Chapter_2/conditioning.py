import numpy as np


def conditioning(a, name):
    det = np.linalg.det(a)
    if abs(det) < 1e-10:
        print("Matrix", name, "is singular, determinant is", det)
    else:
        coeffWellConditioned = 0
        for i in range(len(a)):
            for j in range(len(a)):
                while a[i, j] < 10 * det:
                    coeffWellConditioned += 1
                    break
        coeffIllConditioned = len(a) ** 2 - coeffWellConditioned
        if coeffIllConditioned > coeffWellConditioned:
            conditioningValue = "ill conditioned"
        else:
            conditioningValue = "well conditioned"
        print("Matrix", name, "is", conditioningValue, ", its determinant is", det, "and has", coeffIllConditioned,
              " coefficents "
              "10 times larger than determinan")