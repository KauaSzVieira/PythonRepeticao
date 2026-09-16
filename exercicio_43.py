# DECLARAR
ana: float; maria: float; anos: int
# INÍCIO
ana = 1.10
maria = 1.50
anos = 0

while ana <= maria:
    ana = ana + 0.03
    maria = maria + 0.02
    anos = anos + 1

# EXIBIR
print(anos)
# FIM
