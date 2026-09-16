# DECLARAR
contador: int; soma: float; termo: float
# INÍCIO
contador = 1
soma = 0

while contador <= 15:
    termo = contador / (contador * contador)

    if contador % 2 == 0:
        soma = soma - termo
    else:
        soma = soma + termo

    contador = contador + 1

# EXIBIR
print(soma)
# FIM
