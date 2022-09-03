##Rafaela Ramos dos Santos de Medina
##RU=3608802

# #Variavel Global
valor = 0.08

#--------começo da função feijoada-----

def feijoada():
   while True:
        feijoada = input('escolha a opçao desejada:\nBa - Basica\nPre - Premiun\nSup - Suprema\n>>')
        if feijoada == 'ba':
            return 1.0
        elif feijoada == 'pre':
            print('adicional de 25%')
            return 1.25
        elif feijoada == 'sup':
            print('adicional de  50%')
            return 1.50
        else:
            print('opção invalida! Tente novamente.')
            continue

        #--------fim da função feijoada---------
        #--------começo da função peso(kg)(ml)--
def pesokgml():
    while True:
          peso = float(input('entre com quantidade de feijoada desejada'))
          if (peso  <= 299):
                print('Não aceitamos pedidos menor 300ml!')
          elif (peso > 300) and (peso <= 5000):
                total = peso * valor
                print('voce escolheu {}ml, O valor é de R${:.2f}'.format(peso, total))
                return total
          else:
                (peso < 5000)
                print('nao aceitamos pedidos maior que 5000 ml')
          continue

#--------fim da função peso (kg) (ml)---
#-----menu do restaurante
print('bem vindo ao programa de venda de feijoada da Rafaela Medina!')
print(' ')
print('menu feijoada!')
print(' ')
print('Bá - -Básica  (Feijão + paiol + costelinha)---------------------------------------1000ml==R$ 80.00')
print('Pre - Premium (Feijão + paiol + costelinha + partes de porco)------------------------------add-25%')
print('Sup - Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon)add-50%')
#---chamada das funções e atribuição das variaveis
total = feijoada()
subtotal = pesokgml()
val1 = total * subtotal
val = 0
print('O subtotal é de : R${}'.format(val1))
#--um acumulador para adicionar os acompanhamentos em um loop de repetição

while True:
    acompanhamento = int(input(
        'deseja mais algum acompanhamento?:\n1- 200g de arroz	\n2- 150g de farofa especial\n3- 100g de couve cozida\n4- 1 laranja descascada\n0- Não desejo mais acompanhamentos (encerrar pedido)\n>>'))
    if acompanhamento == 1:
        val = val + 5
    elif acompanhamento == 2:
        val = val + 6
        print('adicional de : R${:.2f}'.format(val))
    elif acompanhamento == 3:
        val = val + 7
        print('adicional de : R${:.2f}'.format(val))
    elif acompanhamento == 4:
        val = val + 3
        print('adicional de : R${:.2f}'.format(val))
    elif acompanhamento == 0:
        break
    else:
        print('opçao invalida , tente novamente!')
    continue

valor_final = val + val1
print('Subtotal é de R${:8.2f}, e o acompanhamento é de R${:8.2f}'.format(val1, val))
print('total é de :R${:8.2f}'.format(valor_final))
print('obrigado por utilizar nossos serviços!')
