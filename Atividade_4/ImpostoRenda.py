#  O IR (Imposto de Renda) é calculado da seguinte forma:
#    se salário-base > 2000, IR = (150) + (salário-base - 2000) * 20%
#    se 1000 < salário-base <= 2000, IR = (salário-base - 1000) * 15%
#    se salário-base <= 1000, IR = 0


def calculaIR(salario):
    IR = 0.0
    if 1000.0 < salario <= 2000.0:
        IR += (salario - 1000.0) * 0.15
    elif salario > 2000.0:
        IR += 150 + (salario - 2000.0) * (0.20)
    elif salario > 3000.0:
        IR += (salario - 3000.0) * (0.05)
    return IR
