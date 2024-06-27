# descrição: implementação da suloção de sistemas pelo método de Seidel
# autor: Julia Pereira

import numpy as np

# formata os números para não usar notação científica e terem somente 4 casas decimais
np.set_printoptions(precision = 4, suppress = True)

# função Método de Seidel
# descrição: implementa os passos do método de Seidel para a solução de sistema
# argumentos:
# (matrix_a): array com os coeficientes de x 
# (vetor_b): array com os coeficientes de y
# (erro_esperado): determina o crtério de parada
# retorno: valores de x que solucionam as equações ou um texto caso não exista convergência
def metodo_jacobi(matrix_a, vetor_b, erro_esperado):
    dimensao = matrix_a.shape[0]

    # verificação de convergência
    for i in range(0, dimensao):
        somatorio = np.sum(np.absolute(matrix_a[i])) - abs(matrix_a[i][i])
        if abs(matrix_a[i][i]) < somatorio:
            return "Não existe convergência. Por favor, alterar a matriz!"
        
    # atribuições inciais
    vetor_x = np.zeros((dimensao, 1))
    erros = np.zeros(dimensao)
    passo = 1

    # iterações
    while(True):
        x_ant = vetor_x.copy()

        # cálculo dos x^k+1
        for i in range(0, dimensao):
            somatorio = np.sum(np.matmul(matrix_a[i], vetor_x)) - matrix_a[i][i] * vetor_x[i]
            vetor_x[i] = (vetor_b[i] - somatorio) / matrix_a[i][i] # aplicação da fórmula para encontrar x^k+1

        erros = np.abs(vetor_x - x_ant) # cálculo dos erros de cada x^k+1

        # mostra os passos até a solução
        print(f'Passo: {passo}')
        print(f'Vetor X: \n{vetor_x}')
        print(f'Erros: \n{erros}\n')

        passo += 1
        
        if np.max(erros) < erro_esperado: # para a iteração assim que o maior erro for menor que o erro esperado
            return vetor_x

c_x = np.array([[10, 3 , 2], [3, 17, 5], [2, -4, 9]])
c_y = np.array([-2, 6, 5])
solucao = metodo_jacobi(c_x, c_y, 0.001)
print(solucao)