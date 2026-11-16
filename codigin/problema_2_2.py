dias = ["Domingo", "Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado"]
temperaturas = []
for i in range(7):
    t = float(input("Temperatura de " + dias[i] + ": "))
    while t < -10 or t > 50:
        print("Temperatura invalida!")
        t = float(input("Temperatura de " + dias[i] + ": "))
    temperaturas.append(t)

for i in range(7):
    print(i, dias[i], temperaturas[i])
maior = temperaturas[0]
menor = temperaturas[0]
indice_maior = 0
alertas = 0

for i in range(7):
    if temperaturas[i] > maior:
        maior = temperaturas[i]
        indice_maior = i
    if temperaturas[i] < menor:
        menor = temperaturas[i]
    if temperaturas[i] > 32:
        alertas = alertas + 1

print("Maior temperatura:", maior)
print("Menor temperatura:", menor)
print("Dias de Alerta de Calor:", alertas)
print("Indice da maior temperatura:", indice_maior)