salario = float(input('Entre com o salário do funcionário:R$'))
ns = salario + (salario * 15 / 100)
print('O novo salário do funcionário, com reajuste de 15 % será de {:.2f}'.format(ns))
