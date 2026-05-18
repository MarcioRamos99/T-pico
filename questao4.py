lista = []

for i in range(10):
    valor = int(input("Digite o numero "))
    
    lista.append(valor)

positivos = 0
negativos = 0
zeros = 0

for i in lista:
    if i > 0 :
        positivos = positivos + 1

    if i < 0 :
        negativos = negativos + 1

    if i == 0 :
        zeros = zeros + 1

print("quantidade de positivos", positivos)
print("quantidade de negativos", negativos)
print("quantidade de zeros", zeros)



