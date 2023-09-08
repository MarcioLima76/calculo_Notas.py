#Aluguel de carros
print('-'*10, 'Aluguel de carros', '-'*10)
km = float(input('Digite a quantidade de KM percorridos:'))
d = int(input('Coloque a quantidade de dias alugado:'))
preço = km*0.15 + d*60
print('o preço a pagar será de R${:.2f}'.format(preço))




