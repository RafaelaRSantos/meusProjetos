#Pizzaria Da Rafaela Ramos dos Santos de Medina
#RU: 3608802

def menu():
        print('='*20,'Cardápio do dia','='*20)
        print('| Código | | Descrição | | Pizza Média | | Pizza Grande |')
        print('|   21   | |Napolitana | |   R$20,00   | |    R$26,00   |')
        print('|   22   | |Margherita | |   R$20,00   | |    R$26,00   |')
        print('|   23   | |Calabresa  | |   R$25,00   | |    R$32,50   |')
        print('|   24   | |Toscana    | |   R$30,00   | |    R$39,00   |')
        print('|   25   | |Portuguesa | |   R$30,00   | |    R$39,00   |')
        print('=========================================================')

print('Pizzaria Da Rafa')
print('bem vindo!')
print(' ')
menu()
valor = 0
while True:
        try:
                codigo = input('Entre com o código da Pizza: ')#entrada do código da pizza.
                tamanho = input('Entre com o tamanaho da Pizza: ')

                #comparação de valores para saber se estao entrando com o codigo certo.
                if codigo == '21'and tamanho == 'm':
                        valor = valor + 20
                        print('subtotal é de : {:8.2f}'.format(valor))
                elif codigo == '22'and tamanho == 'm':
                        valor = valor + 20
                        print('subtotal é de : {:8.2f}'.format(valor))
                elif codigo == '23' and tamanho == 'm':
                        valor = valor + 25
                        print('subtotal é de : {:8.2f}'.format(valor))
                elif codigo == '24' and tamanho == 'm':
                        valor = valor + 30
                        print('subtotal é de : {:8.2f}'.format(valor))
                elif codigo == '25' and tamanho == 'm':
                        valor = valor + 30
                        print('subtotal é de : {:8.2f}'.format(valor))
                #Pizzas Grandes
                # comparação de valores para saber se estao entrando com o codigo certo.
                        valor = valor + 30
                elif codigo == '21' and tamanho == 'g':
                        valor = valor + 26
                        print('subtotal é de : {:8.2f}'.format(valor))
                elif codigo == '22' and tamanho == 'g':
                        valor = valor + 26
                        print('subtotal é de : {:8.2f}'.format(valor))
                elif codigo == '23' and tamanho == 'g':
                        valor = valor + 32.5
                        print('subtotal é de : {:8.2f}'.format(valor))
                elif codigo == '24' and tamanho == 'g':
                        valor = valor + 39
                        print('subtotal é de : {:8.2f}'.format(valor))
                elif codigo == '25' and tamanho == 'g':
                        valor = valor + 39
                        print('subtotal é de : {:8.2f}'.format(valor))
                #se entrar com o codigo errado quebrara loop de reptição.
                else:
                     print('Opção invalida!')
                     continue
                resposta = input('Deseja mais alguma Pizza? (s/n)')

                if resposta == 's':
                        continue
                else:
                        print('Volor total  é de: {:.2f}'.format(valor))
                        print('Obrigado por usar nossos serviços!')
                        break
                #se nao houver problemas, finalizaçao do programa
        except ValueError:
            print('Informe um numero valido')
