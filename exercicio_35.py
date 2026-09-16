# DECLARAR
a: int; b: int; maior: int; menor: int; contador: int; soma: int
# INÍCIO
# LER
a = int(input("Insira o primeiro valor: "))
b = int(input("Insira o segundo valor: "))

if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a

contador = menor + 1
soma = 0

while contador < maior:
    if contador % 2 != 0:
        soma = soma + contador
    contador = contador + 1

# EXIBIR
print(soma)
# FIM
