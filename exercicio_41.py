# DECLARAR
dado1: int; dado2: int
# INÍCIO
dado1 = 1

while dado1 <= 6:
    dado2 = 1

    while dado2 <= 6:
        if dado1 + dado2 == 7:
            print(dado1, dado2)
        dado2 = dado2 + 1

    dado1 = dado1 + 1
# FIM
