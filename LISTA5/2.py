def tabuada(numero):
    print("Tabuada de todas as tabuadas para o número", numero, ":")
    for i in range(1, 11):
        print("\nTabuada do", i, ":")
        for j in range(1, 11):
            print(numero * i, "x", j, "=", (numero * i) * j)

# Exemplo de uso:
tabuada(1)
