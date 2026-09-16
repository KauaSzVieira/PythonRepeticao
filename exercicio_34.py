# DECLARAR
numero: int; contador: int; resultado: int
# INÍCIO
# LER
numero = int(input("Insira um número: "))

contador = 1

while contador <= 10:
    resultado = numero * contador
    print(numero, "x", contador, "=", resultado)
    contador = contador + 1
# FIM
