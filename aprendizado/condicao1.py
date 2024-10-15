name = input("Digite o nome do filme: ")
yearRelease = int(input("Digite o ano de lançamento: "))
rating = float(input("Digite a nota de lançamento: "))

if rating > 8.0 and yearRelease > 2015:
    print(f"O filme {name} é muito bom. Recomendo assistir")
else:
    print(f"O filme {name} ainda não atingiu boa nota.")


