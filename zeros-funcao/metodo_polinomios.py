# Mude os coeficientes e o valor do erro esperados!

# coeficientes = [... ,a5,  a4,  a3,  a2,  a1,  a0]
coeficientes = [2, 5, -15, -35]

def funcao(x):
    y = 0
    for (index, coeficiente) in enumerate(coeficientes):
        # print(index)
        y += (coeficiente * x**(len(coeficientes) - index - 1))
    return round(y, 2)

def define_valor_inicial():
    valor_inicial = 0
    print("x".ljust(10) + "y".ljust(10))
    for x in range(-5, 6):
        y = funcao(x)
        print(f"{x: <10}{y: <10}")

    print("\nEscolha o intervalo:")
    valor_inicial += float(input("Primeiro valor: "))
    valor_inicial += float(input("Segundo valor: "))

    return valor_inicial/2

def tupla_b0_c1(x_i):
    b0 = 0
    c0 = 0
    i = 3

    for coeficiente in coeficientes:
        b_i_ant = b0
        b0 = coeficiente + x_i*b_i_ant

        c1 = c0
        c0 = b0 + x_i*c1

        print(f"b{i}: {b0}")
        print(f"c{i}: {c0}")
        i -= 1
    return (b0, c1)

def mostra_tabela(resultado):
    print("\n" + "n".ljust(3) + "x_i".ljust(12) + "f(x_i)".ljust(15) + "b0".ljust(15) + "c0".ljust(15) + "x_i+1".ljust(15) + "f(x_i+1)".ljust(15) + "erro_esperado".ljust(15) + "erro_real".ljust(15))
    for (index, passo) in enumerate(resultado):
        print(f"{index + 1: <3}{passo[0]:.5f}".ljust(15) + f"{passo[1]:.5f}".ljust(15) + f"{passo[2]:.5f}".ljust(15) + f"{passo[3]:.5f}".ljust(15) + f"{passo[4]:.5f}".ljust(15) + f"{passo[5]:.5f}".ljust(15) + f"{passo[6]}".ljust(15) + f"{passo[7]:.5f}".ljust(15))

def metodo_polinomios():
    x_i = define_valor_inicial()
    erro_esperado = 0.001
    resultado = []

    while True:
        b_0, c_1= tupla_b0_c1(x_i)

        x_i_prox = round(x_i - b_0/c_1, 5)

        f_x_i = funcao(x_i)
        f_x_i_prox = funcao(x_i_prox)

        erro_real = abs(x_i_prox - x_i)

        passo = [x_i, f_x_i, b_0, c_1, x_i_prox, f_x_i_prox, erro_esperado, erro_real]
        resultado.append(passo)

        if (erro_real < erro_esperado):
            break

        x_i = x_i_prox

    mostra_tabela(resultado)
    
metodo_polinomios()