# DECLARAR
a: int; b: int; numero: int; divisor: int; quantidade: int
# INÍCIO
# LER
a = int(input("Insira o primeiro valor: "))
b = int(input("Insira o segundo valor: "))

if a > b:
    a, b = b, a

numero = a
while numero <= b:
    divisor = 1
    quantidade = 0

    while divisor <= numero:
        if numero % divisor == 0:
            quantidade = quantidade + 1
        divisor = divisor + 1

    if quantidade == 2:
        print(numero)

    numero = numero + 1
# FIM
