# DECLARAR
n: int; contador: int; anterior: int; atual: int; proximo: int
# INÍCIO
# LER
n = int(input("Insira N: "))

contador = 1
anterior = 0
atual = 1

while contador <= n:
    print(anterior)
    proximo = anterior + atual
    anterior = atual
    atual = proximo
    contador = contador + 1
# FIM
