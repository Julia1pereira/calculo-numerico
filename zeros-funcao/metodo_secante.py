# Mude a função!

def funcao(x):
    return x**2 + x - 6

def define_intervalo():
    intervalo = []
    print("x".ljust(10) + "y".ljust(10))
    for x in range(-5, 6):
        y = funcao(x)
        print(f"{x: <10}{y: <10}")

    print("\nEscolha o intervalo:")
    intervalo.append(float(input("Primeiro valor: ")))
    intervalo.append(float(input("Segundo valor: ")))

    return intervalo

def mostra_tabela(resultado):
    print("\n" + "n".ljust(3) + "x_i-1".ljust(12) + "x_i".ljust(15) + "f(x_i-1)".ljust(15) + "f(x_i)".ljust(15) + "x_i+1".ljust(15) + "f(x_i+1)".ljust(15) + "erro_esperado".ljust(15) + "erro_real".ljust(15))
    for (index, passo) in enumerate(resultado):
        print(f"{index + 1: <3}{passo[0][0]:.5f}".ljust(15) + f"{passo[0][1]:.5f}".ljust(15) + f"{passo[1]:.5f}".ljust(15) + f"{passo[2]:.5f}".ljust(15) + f"{passo[3]:.5f}".ljust(15) + f"{passo[4]:.5f}".ljust(15) + f"{passo[5]:.5f}".ljust(15) + f"{passo[6]:.5f}".ljust(15))

def metodo_secante(erro_esperado):
    intervalo = define_intervalo()
    resultado = []

    while True:
        f_x_i_ant = funcao(intervalo[0])
        f_x_i = funcao(intervalo[1])

        x_i_prox = intervalo[1] - (f_x_i*(intervalo[0] - intervalo[1]))/(f_x_i_ant - f_x_i)
        f_x_i_prox = funcao(x_i_prox)

        erro_real = abs(x_i_prox - intervalo[1])

        passo = [intervalo.copy(), f_x_i_ant, f_x_i, x_i_prox, f_x_i_prox, erro_esperado, erro_real]
        resultado.append(passo)

        if (erro_real < erro_esperado):
            break

        intervalo[0] = intervalo[1]
        intervalo[1] = x_i_prox

    mostra_tabela(resultado)
    
metodo_secante(0.001)