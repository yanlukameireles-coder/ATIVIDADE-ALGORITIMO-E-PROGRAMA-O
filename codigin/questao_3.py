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

soma = 0
for i in range(6):
    soma = soma + notas[i]
media = soma / 6

acima = 0
print("Media da turma:", media)
print("Notas abaixo da media:")
for i in range(6):
    if notas[i] >= media:
        acima = acima + 1
    else:
        print(notas[i])
print("Alunos acima ou iguais a media:", acima)

for i in range(6):
    if notas[i] < media:
        print("Recuperacao do aluno", i + 1)
        rec = float(input("Digite a nota da recuperacao: "))
        while rec < 0 or rec > 10:
            print("Nota invalida!")
            rec = float(input("Digite a nota da recuperacao: "))
        if rec > notas[i]:
            notas[i] = rec

print("Notas atualizadas:")
for i in range(6):
    print("Aluno", i + 1, ":", notas[i])

soma = 0
for i in range(6):
    soma = soma + notas[i]
print("Nova media:", soma / 6)