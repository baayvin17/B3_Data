import numpy as np

matrix = np.array([
    [12, 45, 78, 80],
    [56, 78, 90, 123],
    [34, 56, 78, 80],
    [45, 67, 89, 100],
    [23, 45, 67, 78],
    [78, 90, 123, 145],
    [56, 78, 90, 123],
    [34, 56, 78, 80]
])

matrix_min = np.min(matrix)
matrix_max = np.max(matrix)

normalized_matrix = (matrix - matrix_min) / (matrix_max - matrix_min) * 255

print("Matrice normalisée (intervalle [0, 255]) :")
print(normalized_matrix)
