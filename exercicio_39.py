# DECLARAR
casa: int; graos: int; total: int
# INÍCIO
casa = 1
graos = 1
total = 0

while casa <= 64:
    total = total + graos
    graos = graos * 2
    casa = casa + 1

# EXIBIR
print(total)
# FIM
