notas = []
for i in range(6):
    nota = float(input("Digite a nota do aluno " + str(i + 1) + ": "))
    while nota < 0 or nota > 10:
        print("Nota invalida!")
        nota = float(input("Digite a nota do aluno " + str(i + 1) + ": "))
    notas.append(nota)

print("Notas:")
for i in range(6):
    print("Aluno", i + 1, ":", notas[i])