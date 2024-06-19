import numpy as np
import matplotlib.pyplot as plt

# formata os números para não usar notação científica e terem somente 4 casas decimais
np.set_printoptions(precision = 4, suppress = True)

class Pontos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coeficientes = None

    def interpolacao_quadratica(self):
        # criação da matrix A
        matrix_A = np.ones((3, 3)) # inicializa a matriz A como uma matriz de zeros 3x3
        matrix_A[0] = np.power(self.x, 2) # primeira linha é o vetor ao quadrado
        matrix_A[1] = self.x # segunda linha e o próprio vetor x
        coeficientes = np.zeros(3) # inicializa o array dos coeficientes

        # determinante da matriz A
        det_A = np.linalg.det(matrix_A)

        # determinante variando a posição do vetor y
        for i in [0, 1, 2]:
            temp_matrix = matrix_A.copy() # para não alterar a matriz original
            temp_matrix[i] = self.y # iguala a linha com o vetor y

            coeficientes[i] = np.linalg.det(temp_matrix) / det_A # calcula o det da matriz com as linhas trocadas

        self.coeficientes = coeficientes # para os métodos de aproximação e geração de gráfico acessem os valores dos coeficientes
        return coeficientes
    
    def aproximacao_valor(self, x):
        return self.coeficientes[0] * np.power(x, 2) + self.coeficientes[1] * x + self.coeficientes[2]
    
    def gerar_grafico(self):
        x = np.linspace(0, 10, 11) # gera um array com valores para x, assim é possível gerar valores de y
        y = self.coeficientes[0] * np.power(x, 2) + self.coeficientes[1] * x + self.coeficientes[2]

        plt.plot(x, y)
        plt.show()

x = np.array([0, np.pi/6, np.pi/4])
y = np.array([[0, 0.328,  0.560]])
f = Pontos(x, y)

print(f.interpolacao_quadratica())
f.gerar_grafico()