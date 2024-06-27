# Mude a função!

def funcao(x):
    return 2*x**3 - 7*x**2 + 3*x +  21

def define_intervalo():
    intervalo = []
    print("x".ljust(5) + "y".ljust(5))
    for x in range(-5, 6):
        y = funcao(x)
        print(f"{x: <5}{y: <5}")

    print("\nEscolha o intervalo:")
    intervalo.append(int(input("Primeiro valor: ")))
    intervalo.append(int(input("Segundo valor: ")))

    return intervalo

def mostra_tabela(resultado):
    print("\n" + "n".ljust(3) + "a".ljust(12) + "b".ljust(15) + "f_a".ljust(15) + "f_b".ljust(15) + "x_ns".ljust(15) + "f_x_ns".ljust(15) + "erro_esperado".ljust(15) + "erro_real".ljust(15))
    for (index, passo) in enumerate(resultado):
        print(f"{index + 1: <3}{passo[0][0]:.5f}".ljust(15) + f"{passo[0][1]:.5f}".ljust(15) + f"{passo[1]:.5f}".ljust(15) + f"{passo[2]:.5f}".ljust(15) + f"{passo[3]:.5f}".ljust(15) + f"{passo[4]:.5f}".ljust(15) + f"{passo[5]:.5f}".ljust(15) + f"{passo[6]:.5f}".ljust(15))

def metodo_bissecao(erro_esperado):
    intervalo = define_intervalo()
    resultado = []

    while True:
        erro_real = (intervalo[1] - intervalo[0])/2

        x_ns = (intervalo[0] + intervalo[1])/2
        f_x_ns = funcao(x_ns)

        f_a = funcao(intervalo[0])
        f_b = funcao(intervalo[1])

        passo = [intervalo.copy(), f_a, f_b, x_ns, f_x_ns, erro_esperado, erro_real]
        resultado.append(passo)

        if (erro_real < erro_esperado):
            break

        if (f_a*f_x_ns > 0):
            intervalo[0] = x_ns
        else:
            intervalo[1] = x_ns

    mostra_tabela(resultado)
    
metodo_bissecao(0.001)