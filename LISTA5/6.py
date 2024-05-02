import random

# Função para abrir uma caixa e obter um item
def abrir_caixa(inventario):
    # Probabilidade de obtenção de cada tipo de item
    probabilidade = random.randint(1, 100)
    if probabilidade <= 80:
        inventario['comum'] += 1
        print("Você coletou 1 item comum!")
    elif probabilidade <= 99:
        inventario['raro'] += 1
        print("Você coletou 1 item raro!")
    else:
        inventario['lendario'] += 1
        print("Você coletou 1 item lendário!")

# Função para consultar os itens coletados
def consultar_itens(inventario):
    print("Itens comuns:", inventario['comum'])
    print("Itens raros:", inventario['raro'])
    print("Itens lendários:", inventario['lendario'])

# Função principal
def main():
    inventario = {'comum': 0, 'raro': 0, 'lendario': 0}

    while True:
        print("\n1 - Abrir uma caixa")
        print("2 - Consultar itens")
        print("0 - Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            abrir_caixa(inventario)
        elif opcao == 2:
            consultar_itens(inventario)
        elif opcao == 0:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Execução do programa
if __name__ == "__main__":
    main()
