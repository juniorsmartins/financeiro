import os

"""
Consultar funcionalidades do módulo os
"""

line = "*"

# Retornar pasta atual
print(os.getcwd())

print(line*75)

# Listar arquivos e pastas
print(os.listdir())

print(line*75)

# Versão do Sistema Operacional
os.system('cat /etc/os-release')

print(line*75)

# Configurações da máquina
os.system('uname -a')

print(line*75)

# Limpar tela do terminal
# os.system('clear')

# Desligar o computador - padrão em 60 segundos
# os.system('shutdown /s')

# Cancelar o desligamento
# os.system('shutdown /a')

# Desligar o computador imediatamente
# os.system('shutdown /s /t 0')

# Desligar o computador em 1 hora
# os.system('shutdown /s /t 3600')


