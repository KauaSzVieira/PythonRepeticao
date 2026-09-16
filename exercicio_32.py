# DECLARAR
numero: int; fatorial: int; contador: int
# INÍCIO
# LER
numero = int(input("Insira um número inteiro: "))

fatorial = 1
contador = 1

while contador <= numero:
    fatorial = fatorial * contador
    contador = contador + 1

# EXIBIR
print(fatorial)
# FIM
