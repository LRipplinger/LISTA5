import random

def sorteio(inicio, fim):
    return random.randint(inicio, fim)

# Exemplo de uso:
inicio = int(input("Digite o valor inicial do intervalo: "))
fim = int(input("Digite o valor final do intervalo: "))
numero_sorteado = sorteio(inicio, fim)
print("Número sorteado:", numero_sorteado)
