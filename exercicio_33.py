# DECLARAR
n: int; contador: int; soma: float
# INÍCIO
# LER
n = int(input("Insira N: "))

contador = 1
soma = 0

while contador <= n:
    soma = soma + 1 / contador
    contador = contador + 1

# EXIBIR
print(soma)
# FIM
