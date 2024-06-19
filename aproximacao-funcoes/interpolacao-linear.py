import numpy as np
import matplotlib.pyplot as plt

# formata os números para não usar notação científica e terem somente 4 casas decimais
np.set_printoptions(precision = 4, suppress = True)

class Pontos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coeficientes = None

    def interpolacao_linear(self):
        # criação da matrix A
        matrix_A = np.ones((2, 2)) # inicializa a matriz A como uma matriz de zeros 2x2
        matrix_A[0] = self.x # iguala a primeira linha com o vetor x, aqui uso a propriedade do det da matriz transposta ser igual a original
        coeficientes = np.zeros(2) #inicializa o array dos coeficientes

        # determinante da matriz A
        det_A = np.linalg.det(matrix_A)

        # determinante variando a posição do vetor y
        for i in [0, 1]:
            temp_matrix = matrix_A.copy() # para não alterar a matriz A original
            temp_matrix[i] = self.y # iguala a linha com o vetor y

            coeficientes[i] = np.linalg.det(temp_matrix) / det_A # calcula o determinante e salva no np.array

        self.coeficientes = coeficientes # para as funções de gerar gráfico e aproximação conseguirem acessar os coeficientes
        return coeficientes
    
    def aproximacao_valor(self, x):
        return self.coeficientes[0] * x + self.coeficientes[1]
    
    def gerar_grafico(self):
        x = np.linspace(0, 1, 11) # gera uma sequência de valores para x, assim é possível gerar valores de y
        y = self.coeficientes[0] * x + self.coeficientes[1] # calcula os valores de y

        plt.plot(x, y)
        plt.show()

x = np.array([0, 1])
y = np.array([1.35, 2.94])
f = Pontos(x, y)

print(f.interpolacao_linear())
print(f.aproximacao_valor(0.73))
f.gerar_grafico()