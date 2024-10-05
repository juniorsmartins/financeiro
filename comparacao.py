num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2

print(f"O primeiro número é maior que o segundo: {bigger}")
print(f"O primeiro número é menor que o segundo: {smaller}")
print(f"O primeiro número é igual ao segundo: {equal}")
print(f"O primeiro número é diferente do segundo: {different}")

bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print(f"O primeiro número é maior ou igual ao segundo: {bigger_equal}")
print(f"O primeiro número é menor ou igual ao segundo: {smaller_equal}")

