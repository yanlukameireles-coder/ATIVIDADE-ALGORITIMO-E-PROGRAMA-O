# Atividade de Algoritmos - problema1_questao2

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