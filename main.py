from task import Task

if __name__ == '__main__':
    task2 = Task()
    task2.configure_parameters(
        a=0,
        b=2,
        N=101,
        omega=3
    )
    task2.configure_boundary_conditions(
        left=0,
        right=1
    )
    task2.execute()
    task2.write_file('../res/result.txt')

# from progonka import Progonka
# import numpy as np
#
# a = 0
# b = 2
# N = 101
# delta_x = (b - a) / (N - 1)
# omega = 3
# p1 = 0
# pNd = 1
#
#
# def get_c(x):
#     return 1
#
#
# alpha_1 = -1 / delta_x
# alpha_2 = delta_x / 6
#
# beta_1 = 2 / delta_x
# beta_2 = (2 * delta_x) / 3
#
# A = [alpha_1 + ((1j * omega) / (get_c(i) ** 2)) * alpha_2 for i in range(N - 1)]
# B = [beta_1 + ((1j * omega) / (get_c(i) ** 2)) * beta_2 for i in range(N)]
#
# B[0] = B[0] / 2
# B[-1] = B[-1] / 2
#
# # Граничные условия
# A[0] = 0
# B[0] = 1
#
# D = np.zeros((N,))
# D[0] = p1
# D[-1] = pNd
#
# progonka = Progonka()
# progonka.configure(A, B, A, D)
# progonka.execute()
# res = progonka.answer
#
# with open("../res/result.txt", 'w') as file:
#     for i in range(len(res)):
#         print(f"{delta_x * i} {abs(res[i])}\n")
#         file.write(f"{delta_x * i} {abs(res[i])}\n")
