def media_unisinos(nota_grau_a, nota_grau_b):
    peso_grau_a = 0.4
    peso_grau_b = 0.6
    media_final = (nota_grau_a * peso_grau_a) + (nota_grau_b * peso_grau_b)
    return media_final

def main():
    # Solicitar notas do usuário
    nota_grau_a = float(input("Digite a nota do Grau A: "))
    nota_grau_b = float(input("Digite a nota do Grau B: "))

    # Calcular e exibir resultado do Grau Final
    resultado_final = media_unisinos(nota_grau_a, nota_grau_b)
    print("Resultado do Grau Final:", resultado_final)

# Chamar a função principal
if __name__ == "__main__":
    main()
