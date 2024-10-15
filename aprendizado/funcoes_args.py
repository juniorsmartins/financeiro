# Função para imprimir nome completo
def full_name(first_name, last_name):
    print(f"O nome é: {first_name} {last_name}")

full_name("Holga", "Weiss")

# Função para somar dois números
def sum_numbers(a, b):
    return a + b 

print(f"A soma é: {sum_numbers(2, 5)}")

# Função com parâmetro default
def address(country="Brasil"):
    print(f"Moro em: {country}")

address()
address("Canadá")

