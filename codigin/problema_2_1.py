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