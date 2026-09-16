# DECLARAR
base: float; expoente: int; resultado: float; contador: int
# INÍCIO
# LER
base = float(input("Insira a base: "))
expoente = int(input("Insira o expoente: "))

resultado = 1
contador = 1

while contador <= expoente:
    resultado = resultado * base
    contador = contador + 1

# EXIBIR
print(resultado)
# FIM
