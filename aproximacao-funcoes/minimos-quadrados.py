import numpy as np
import matplotlib.pyplot as plt

# formata os números para não usar notação científica e terem somente 4 casas decimais
np.set_printoptions(precision = 4, suppress = True)

class Pontos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coeficientes = None
        self.phi_x = None

    def gerar_grafico_pontos(self):
        plt.plot(self.x, self.y, 'bo')
        plt.show()

    def quadrados_minimos(self, forma):

        if forma == 'l':
            # valores para a construção da matriz A e vetor Y
            m = self.x.shape[0]
            soma_x = np.sum(self.x)
            soma_y = np.sum(self.y)
            soma_x2 = np.sum(np.power(x, 2))
            soma_xy = np.sum(x * y)

            matriz_A = np.round(np.array([[m, soma_x], [soma_x, soma_x2]]), 4) # construção da mattriz A
            vetor_Y = np.round(np.array([soma_y, soma_xy]), 4)

            print(f"Matriz A: {np.round(matriz_A, 3)}", end = '\n')
            print(f"Matriz Y: {np.round(vetor_Y, 3)}", end = '\n\n')

            det_A = np.linalg.det(matriz_A)
            self.coeficientes = np.zeros(2) # inicializa o array dos coeficientes

            for i in [0, 1]:
                temp_a = matriz_A.copy()
                temp_a[i] = vetor_Y

                self.coeficientes[i] = np.linalg.det(temp_a) / det_A

            return self.coeficientes
        
        elif forma == 'q':
            m = x.shape[0]
            soma_x = np.sum(x)
            soma_y = np.sum(y)
            soma_x2 = np.sum(np.power(x, 2))
            soma_x3 = np.sum(np.power(x, 3))
            soma_x4 = np.sum(np.power(x, 4))
            soma_xy = np.sum(x * y)
            soma_x2y = np.sum(np.power(x, 2) * y)

            matriz_A = np.array([[m, soma_x, soma_x2],
                                [soma_x, soma_x2, soma_x3],
                                [soma_x2, soma_x3, soma_x4]])

            vetor_Y = np.array([soma_y, soma_xy, soma_x2y])

            print("Matriz A:")
            print(matriz_A)

            print("Vetor Y:")
            print(vetor_Y)

            det_A = np.linalg.det(matriz_A)
            self.coeficientes = np.zeros(3)

            for i in [0, 1, 2]:
                temp_a = matriz_A.copy()
                temp_a[i] = vetor_Y

                self.coeficientes[i] = np.linalg.det(temp_a) / det_A

            return self.coeficientes
    
    def quadrado_residuos(self):
        self.phi_x = self.coeficientes[0] * np.power(self.x, 0)

        for i in range(1, self.coeficientes.shape[0]):
            self.phi_x += self.coeficientes[i] * np.power(self.x, i)

        residuos = np.sum(np.power(self.y - self.phi_x, 2))

        return residuos
    
    def aproximacao_valor(self, x):
        if (self.coeficientes.shape[0] == 2): # verifica se a equação é linear
            return np.sum(self.coeficientes * np.array([1, x]))
        return np.sum(self.coeficientes * np.array([1, x, x*x]))
    
    def gerar_grafico_comparacao(self):
        plt.plot(self.x, self.y, 'bo')
        plt.plot(self.x, self.phi_x, 'ro-')

        plt.show()


x = np.array([6.2, 15.3, 20.1, 27.3, 32.4, 38.9, 41.5, 47.5])
y = np.array([21.2, 43.2, 49.7, 56.3, 57.9, 57.2, 55.2, 45])

f = Pontos(x, y)

print(f.quadrados_minimos('q'), f.quadrado_residuos())

print(f.aproximacao_valor(25))
print(f.aproximacao_valor(47.5) - 45)