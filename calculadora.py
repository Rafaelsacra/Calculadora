# Função para somar
def somar(a, b):
    return a + b

# Função para subtrair
def subtrair(a, b):
    return a - b

# Função para multiplicar
def multiplicar(a, b):
    return a * b

# Função para dividir
def dividir(a, b):
    if b == 0:
        return "Erro! Divisão por zero."
    return a / b

# Função que exibe o menu e retorna a escolha do usuário
def exibir_menu():
    print("\n--- Calculadora ---")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

    escolha = input("Escolha a operação (1/2/3/4/5): ")
    return escolha

# Função principal para controlar a execução da calculadora
def calculadora():
    while True:  # Loop para manter o programa rodando até o usuário decidir sair
        escolha = exibir_menu()

        if escolha == '5':  # Opção de saída
            print("Saindo da calculadora. Até logo!")
            break

        # Verifica se a escolha é válida
        if escolha not in ['1', '2', '3', '4']:
            print("Escolha inválida! Tente novamente.")
            continue

        # Solicitar os números ao usuário
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, insira valores numéricos válidos.")
            continue  # Se houver erro na entrada, reinicia o loop

        # Realiza a operação de acordo com a escolha do usuário
        if escolha == '1':
            resultado = somar(num1, num2)
            print(f"{num1} + {num2} = {resultado}")
        elif escolha == '2':
            resultado = subtrair(num1, num2)
            print(f"{num1} - {num2} = {resultado}")
        elif escolha == '3':
            resultado = multiplicar(num1, num2)
            print(f"{num1} * {num2} = {resultado}")
        elif escolha == '4':
            resultado = dividir(num1, num2)
            print(f"{num1} / {num2} = {resultado}")

# Rodar a função calculadora
if __name__ == "__main__":
    calculadora()
