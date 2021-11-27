import numpy as np

from progonka import Progonka


class Task:
    a = 0
    b = 0
    N = 0
    delta_x = 0
    omega = 0
    A = []
    B = []
    D = np.array([])
    answer = np.array([])

    def configure_parameters(self, a, b, N, omega):
        self.a = a
        self.b = b
        self.N = N
        self.delta_x = (b - a) / (N - 1)
        self.omega = omega

    def configure_boundary_conditions(self, left, right):
        self.D = np.zeros((self.N,))
        self.D[0] = left
        self.D[-1] = right

    def get_c(self, x):
        return 1

    def execute(self):
        alpha_1 = -1 / self.delta_x
        alpha_2 = self.delta_x / 6

        beta_1 = 2 / self.delta_x
        beta_2 = (2 * self.delta_x) / 3

        self.A = [alpha_1 + ((1j * self.omega) / (self.get_c(i*self.delta_x) ** 2)) * alpha_2 for i in range(self.N - 1)]
        self.B = [beta_1 + ((1j * self.omega) / (self.get_c(i*self.delta_x) ** 2)) * beta_2 for i in range(self.N)]

        # Граничные условия
        self.A[0] = 0
        self.B[0] = 1

        self.B[0] = self.B[0] / 2
        self.B[-1] = self.B[-1] / 2

        progonka = Progonka()
        progonka.configure(self.A, self.B, self.A, self.D)
        progonka.execute()
        self.answer = progonka.answer

    def write_file(self, filename):
        with open(filename, 'w') as file:
            for i in range(len(self.answer)):
                print(f"{self.delta_x * i} {abs(self.answer[i])}\n")
                file.write(f"{self.delta_x * i} {abs(self.answer[i])}\n")
