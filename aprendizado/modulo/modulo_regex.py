import re

texto = "Udemy - uma plataforma de muitos cursos."

# Índice inicial e final de palavras (o 'r' significa uma raw string - string bruta)
match = re.search(r'muitos cursos', texto)
print(f"Índice inicial: {match.start()} e índice final: {match.end()}")

# Buscar índice do ponto
site = 'https://udemy.com'
match = re.search(r'\.', site)
print(match)

# Buscar lista de caracteres dentro de frase
pattern = "[g-m]"
result = re.findall(pattern, texto)
print(result)

# Verificar início de string (se possui a letra maiúscula indicada)
rule = r'^A' # A maiúsculo
phrases = ['A casa está suja', 'O dia está lindo', 'Vamos passear']
for f in phrases:
    if re.match(rule, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Não corresponde: {f}")

# Verificar final de string (se termina com ponto de exclamação)
rule_end = r'!$'
phrase = "O dia está lindo!"
match = re.search(rule_end, phrase)
if match:
    print("Sim, corresponse")
else:
    print("Não corresponde")


