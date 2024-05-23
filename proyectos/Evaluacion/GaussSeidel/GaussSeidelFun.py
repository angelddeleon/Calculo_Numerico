import numpy as np

def gauss_seidel(A, b, x0, epsilon=1e-6 , max_iterations= 100):
    n = len(A)
    x = x0.copy()

    for i in range(max_iterations):
        x_new = np.zeros(n)
        for j in range(n):
            s1 = np.dot(A[j, :j], x_new[:j])
            s2 = np.dot(A[j, (j+1):], x[(j + 1):])
            x_new[j] = (b[j] - s1 -s2) / A[j,j]

        if np.linalg.norm(x_new - x) < epsilon:
            break

        x = x_new.copy()

    return x

A = np.array([[4, -1, 1], [-1, 4, -2], [1,-2,4]])
b = np.array([12, -1, 5])
x0 = np.zeros(3)
epsilon = 1e-6
max_iterations = 100




