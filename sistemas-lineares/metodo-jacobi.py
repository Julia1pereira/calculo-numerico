import numpy as np

def metodo_jacobi(matrix_a, vetor_b):
    dimensao = matrix_a.shape[0]
    # verificação de convergência
    for i in range(0, dimensao):
        somatorio = np.sum(np.absolute(matrix_a[i])) - abs(matrix_a[i][i])
        if abs(matrix_a[i][i]) < somatorio:
            return "Não existe convergência"
        
    # atribuição incial
    vetor_x = np.zeros((dimensao, 1))

    erro_esperado = 0.001
    erros = np.zeros(dimensao)

    passo = 1

    # iterações
    while(True):
        x_ant = vetor_x.copy()

        # cálculo dos x^k+1
        for i in range(0, dimensao):
            somatorio = np.sum(np.matmul(matrix_a[i], x_ant)) - matrix_a[i][i] * vetor_x[i]
            vetor_x[i] = (vetor_b[i] - somatorio) / matrix_a[i][i] # aplicação da fórmula para encontrar x^k+1

            erros[i] = abs(vetor_x[i] - x_ant[i]) # cálculo dos erros de cada x^k+1

        print(f'\nPasso: {passo}')
        print(f'Vetor X: \n{np.round(vetor_x, 4)}')
        print(f'Erros: \n{np.round(erros, 4)}')

        passo += 1
        
        if np.max(erros) < erro_esperado: # para a iteração assim que o maior erro for menor que o erro esperado
            return vetor_x


c_x = np.array([[10, 3 , 2], [3, 17, 5], [2, -4, 9]])
c_y = np.array([-2, 6, 5])
solucao = metodo_jacobi(c_x, c_y)

print(f'Solucão: {solucao}')
