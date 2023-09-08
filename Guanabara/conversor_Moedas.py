#Conversor de Moedas
print('-'*10, 'Conversor de Moedas', '-'*10)
real = float(input('Digite o valor que você tem em reais: R$'))
dolar = real / 5.67
euro = real / 6.72
libra = real / 7.98
print('Você tem R$ {:.2f}, que é  equivalente a $ {:.2f} dolares ,  {:.2f} Euros ou {:.2f} Libras '.format(real, dolar, euro, libra))

