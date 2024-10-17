import hashlib

line = "*"

# Verificar algoritmos disponíveis
print(hashlib.algorithms_available)
print(line*75)

# Verificar algoritmos de acordo com o sistema operacional
print(hashlib.algorithms_guaranteed)
print(line*75)

# Utilizar SHA256
algorithm = hashlib.sha256()
print(algorithm.digest())
message = "A melhor forma de prever o futuro é criá-lo.".encode()
algorithm.update(message)
print(algorithm.hexdigest())
print(line*75)

# Utilizar o MD5
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())
print(line*75)

