# DECLARAR
contador: int; soma: float
# INÍCIO
contador = 1
soma = 0

while contador <= 50:
    soma = soma + contador / (2 * contador + 1)
    contador = contador + 1

# EXIBIR
print(soma)
# FIM
