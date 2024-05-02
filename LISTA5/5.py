def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero."

def main():
    print("Bem-vindo à calculadora simples!")
    print("Escolha a operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")

    opcao = int(input("Digite o número da operação desejada: "))

    if opcao in [1, 2, 3, 4]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == 1:
            print("Resultado da soma:", somar(num1, num2))
        elif opcao == 2:
            print("Resultado da subtração:", subtrair(num1, num2))
        elif opcao == 3:
            print("Resultado da multiplicação:", multiplicar(num1, num2))
        elif opcao == 4:
            print("Resultado da divisão:", dividir(num1, num2))
    else:
        print("Opção inválida. Por favor, escolha uma operação válida.")

# Chamada da função principal
main()
