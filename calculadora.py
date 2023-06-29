def potencia(a, b):
    return a ** b

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

# Exemplo de uso da calculadora
numero1 = float(input("Digite o 1° número: "))
numero2 = float(input("Digite o 2° número: "))

print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite o número da operação desejada: ")

if opcao == "1":
    resultado = soma(numero1, numero2)
    print("Resultado: ", resultado)
elif opcao == "2":
    resultado = subtracao(numero1, numero2)
    print("Resultado: ", resultado)
elif opcao == "3":
    resultado = multiplicacao(numero1, numero2)
    print("Resultado: ", resultado)
elif opcao == "4":
    resultado = divisao(numero1, numero2)
    print("Resultado: ", resultado)
else:
    print("Opção inválida!")
