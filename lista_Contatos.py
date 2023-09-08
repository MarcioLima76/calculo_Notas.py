print('Lista de Contatos')


while True:
    nome = str(input(' Digite o nome do aluno:'))
    if nome.isalpha():
        nome.isalpha() == True
    print('nome {} registrado com sucesso'.format(nome))
    else:
    print(str(input('Dados inválidos. Por favor, informe o nome do cliente:')))


    sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MnFf':
        sexo = str(input('Dados inválidos. Por favor, informe seu sexo:')).strip().upper()[0]
        print('Sexo {} registrado com sucesso'.format(sexo))




