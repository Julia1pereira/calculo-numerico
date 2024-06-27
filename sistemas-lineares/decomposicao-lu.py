# descrição: implementação da técnica de decomposição LU para solução de sistemas de 2 ou mais incógnitas
# autor: Julia Pereira

import numpy as np
from numpy.linalg import inv

# formata os números para não usar notação científica e terem somente 4 casas decimais
np.set_printoptions(precision = 4, suppress = True)

# função de decomposição LU
# descrição: implementa os passos da decomposição LU para a solução de sistema
# argumentos:
# (matrix_a): array com os coeficientes de x 
# (vetor_b): array com os coeficientes de y
# retorno: valores de x que solucionam as equações
def decomposicao_LU(matrix_a, vetor_b):
    dimensao = matrix_a.shape[0] # descobre a dimesão do sistema
    matrix_L = np.float32(np.identity(dimensao)) # inicializa a matriz L com uma matriz identidade
    matrix_U = np.float32(matrix_a.copy())

    # gerando as matrizes U e L
    for iteracao in range(0, dimensao - 1):
        for linha in range(iteracao, dimensao - 1):
            divisor = matrix_U[(linha + 1), iteracao] / matrix_U[iteracao, iteracao] # calcula do divisor que zera o elemento abaixo
            matrix_L[iteracao, linha + 1] = divisor # adiciona o divisor na matrix L
            for coluna in range(iteracao, dimensao):
                matrix_U[linha + 1, coluna] -= divisor * matrix_U[iteracao, coluna] # atualiza a linha de baixo fazendo: linha_baixo - divisor * linha_cima

    # gerando o vetor y
    inversa_L = inv(matrix_L.transpose()) # a lógica para gerar a matriz L gera uma transposta, por isso matrix_L.transpose()
    vetor_y = np.matmul(inversa_L, vetor_b) # vetor_y = inversa da matriz l * vetor_b

    # gerando o vetor x
    inversa_U = inv(matrix_U)
    vetor_x = np.matmul(inversa_U, vetor_y) # vetor_x = inversa da matriz u * vetor_y

    print('Matrix L:')
    print(matrix_L)
    print('Matrix U:')
    print(matrix_U)

    return vetor_x


c_x = np.array([[1, 1, 2], [2, -1, -1], [1, -1 , -1]])
c_y = np.array([4, 0, -1])
solucao = decomposicao_LU(c_x, c_y)

print(f'Solucão: {solucao}')