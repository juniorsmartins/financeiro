"""
*args - utilizamos quando não temos certeza de quantos argumentos queremos ter numa função.
- os argumentos são passados como tupla
"""

# Soma de números
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"A soma é: {sum_total}")

sum(7)
sum(5,2)
sum(3,2,1,1)

"""
**kwargs - além dos valores, podemos passar também as respectivas chaves para cada argumento.
- os argumentos são passados como dicionário
"""

# Apresentação de cursos
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")
    print("\n")

print("\nLista de Cursos\n")
presentation(name="Python", category="Backend", level="Iniciante")
presentation(name="Visão Computacional com Python", category="IA", level="Avançado")
presentation(name="Dashboards com Dash", category="Data Science", level="Intermediário")

