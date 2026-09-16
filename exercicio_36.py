# DECLARAR
n: int; contador: int; fatorial: int; soma: float
# INÍCIO
# LER
n = int(input("Insira N: "))

contador = 0
fatorial = 1
soma = 1

while contador < n:
    contador = contador + 1
    fatorial = fatorial * contador
    soma = soma + 1 / fatorial

# EXIBIR
print(soma)
# FIM
