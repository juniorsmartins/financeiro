num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operation = input("Digite a operação a ser realizada (+ - * /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("Operação inválida!")
    result = 0

print(f"O resultado é: {result:.2f}")


