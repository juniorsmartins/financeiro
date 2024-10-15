# Função para imprimir
def welcome():
    print("Bem-vindo!")

welcome()
welcome()

# Função para calcular média de notas
def calculate_average():
    num_ratings = int(input("Digite quantas avaliações deseja fazer por filme: "))
    total = 0
    for _ in range(num_ratings):
        note = float(input("Digite a nota para o filme: "))
        total += note

    if num_ratings > 0:
        average = total / num_ratings
    else:
        average = 0

    return average

print(f"A nota média das avaliações é: {calculate_average():.1f}")



