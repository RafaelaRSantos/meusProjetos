# Projeto de APP de desconto
#Rafaela ramos dos santos medina
#RU 3608802
import math
print('Bem vindo ao APP de Rafaela Ramos dos Santos Medina')
print(' ')

        # Variaveis globais

valor = int
produto = int
total = int

while True:
        try:

            #Entreda de valores

            print('Entre com a quantidade de produto"s"e o valor')
            print(' ')
            print('para Calcular qual sera o seu desconto.')
            valor = float(input('Informe o valor do produto: '))
            produto = int(input('Informe a quantidade de produto"s": '))

            total = produto * valor

            print('O valor total é de {}'.format(total))

            if 0 <= produto <= 4:
                print('Você so recebera desconto acima de 4 produtos')
            elif 5 >= produto <= 19:
                print('O valor com o desconto é de:{}.(3% de desconto)'.format(total - total * 0.03))
            elif 20 >= produto <= 99:
                print('O valor com o desconto é de:{}.(6% de desconto)'.format(total - total * 0.06))
            else:
                produto >= 100
                print('O valor com o desconto é de:{}(10% de desconto)'.format(total - total * 0.1))
        except ValueError:
            print('Informe um numero valido')

        break