lista = []

for i in range(6):
    valor = float(input("Digite sua nota: "))
    lista.append(valor)


    

soma = sum(lista)
media = soma / len(lista)
quantidade=0
acima_media=[]

for i in lista:
    if i > media:
        quantidade = quantidade+1
        acima_media.append(i)

print("media: ", media)
print("quantidade de notas acima da media: ", quantidade)
print("notas acima da media: ", acima_media)
