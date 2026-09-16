# DECLARAR
numero: int; contador: int; maior: int; menor: int
# INÍCIO
contador = 1
maior = 0
menor = 0

while contador <= 100:
    numero = int(input("Insira um número positivo: "))

    if contador == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    contador = contador + 1

# EXIBIR
print("Maior:", maior)
print("Menor:", menor)
# FIM
