# Mude a função e as derivadas!

import math

def funcao(x):
    return 2*x - math.sin(x) - 4

def primeira_derivada(x):
    return 2 - math.cos(x)

def segunda_derivada(x):
    return math.sin(x)

def define_valor_inicial():
    intervalo = []
    print("x".ljust(10) + "y".ljust(10))
    for x in range(-5, 6):
        y = funcao(x)
        print(f"{x: <10}{y: <10}")

    print("\nEscolha o intervalo:")
    intervalo.append(int(input("Primeiro valor: ")))
    intervalo.append(int(input("Segundo valor: ")))

    f_a = funcao(intervalo[0])
    f_a2 = segunda_derivada(intervalo[0])
    f_b = funcao(intervalo[1])
    f_b2 = segunda_derivada(intervalo[1])

    if (f_a*f_a2 > 0):
        return f_a
    elif (f_b*f_b2 > 0):
        return f_b

def mostra_tabela(resultado):
    print("\n" + "n".ljust(3) + "x_i".ljust(12) + "f(x_i)".ljust(15) + "f'(x_i)".ljust(15) + "x_i+1".ljust(15) + "f(x_i+1)".ljust(15) + "erro_esperado".ljust(15) + "erro_real".ljust(15))
    for (index, passo) in enumerate(resultado):
        print(f"{index + 1: <3}{passo[0]:.5f}".ljust(15) + f"{passo[1]:.5f}".ljust(15) + f"{passo[2]:.5f}".ljust(15) + f"{passo[3]:.5f}".ljust(15) + f"{passo[4]:.5f}".ljust(15) + f"{passo[5]:.5f}".ljust(15) + f"{passo[6]:.5f}".ljust(15))

def metodo_newton(erro_esperado):
    x_i = define_valor_inicial()
    resultado = []

    while True:
        f_x_i = funcao(x_i)
        f_x_i1 = primeira_derivada(x_i)

        x_i_prox = x_i -(f_x_i/f_x_i1)

        erro_real = abs(x_i_prox - x_i)

        passo = [x_i, f_x_i, f_x_i1, x_i_prox, funcao(x_i_prox), erro_esperado, erro_real]
        resultado.append(passo)

        if (erro_real < erro_esperado):
            break

        x_i = x_i_prox

    mostra_tabela(resultado)
    
metodo_newton(0.001)