listaProdutos = [] #aluna : Rafaela ramos dos santos de medina , RU 3608802
def cadastrarProduto(codigo):#codificar uma função cadastrarProdutos (código)
  print('Você selecionou a opção de Cadastrar Produto')
  print('O código do produto é: {:0>3}'.format(codigo))
  nome = input('Entre com o nome do produto:')
  fabricante = input('Entre com o fabricante da produto:')
  valor = float(input('Entre com o valor R$ da produto:'))
  dicionarioProdutos = {'codigo'   : codigo,
                         'nome' : nome,
                         'fabricante': fabricante,
                         'valor': valor}
  listaProdutos.append(dicionarioProdutos.copy())
def consultarProduto():#consulta de produtos , por codigo fabricante,  lista de produtos.
  while True:
    try:
      print('Você Selecionou a Opção de Consultar Produto')
      opConsultar = int(input('Entre com a opção desejada\n1- Consultar Todos os Produtos\n2- Consultar Produtos por Código\n3- Consultar Produtos por Fabricante\n4- Retornar\n-->'))
      if opConsultar == 1:
        print('-' * 20)
        for produtos in listaProdutos:
            for key, value in produtos.items():
              print('{} : {}'.format(key,value))
            print('-' * 20)
      elif opConsultar == 2:
        print('Você Selecionou a Opção Produto por Código')
        entrada = int(input('Digite o Código: '))
        print('-' * 20)
        for produtos in listaProdutos:
          if(produtos['codigo'] == entrada):
            for key, value in produtos.items():
              print('{} : {}'.format(key,value))
            print('-' * 20)
      elif opConsultar == 3:
        print('Você Selecionou a Opção Produtos por Fabricante')
        entrada = input('Digite o Fabricante: ')
        print('-' * 20)
        for produto in listaProdutos:
          if(produto['fabricante'] == entrada):
            for key, value in produto.items():
              print('{} : {}'.format(key,value))
            print('-' * 20)
      elif opConsultar == 4:
        break
      else:
        print('Por favor digite somente o que pede')
        continue
    except ValueError:
      print('Por Favor pare de digitar números que não existe...')
      continue
def removerProduto():#aqui é a funçao de remover produtos , usuari entra como codigo do produto a ser removido .
    print('Você Selecionou o Remover Produto')
    entrada = int(input('Digite o Código do produto que irá remover: '))
    for produtos in listaProdutos:
      if(produtos['codigo'] == entrada):
        listaProdutos.remove(produtos)
    else:
      print('Você removeu o código.')
print('Bem-vindo ao Controle de Estoque da Mercearia (Rafaela ramos dos santos, Ru3608802  )')
registroProdutos = 0
while True:
    try:
      opcao = int(input('Digite a opção desejada:\n1- Cadastrar Produtos\n2- Consultar Produtos\n3- Remover Produtos\n4- Sair\n-->'))
      if opcao == 1:
        registroProdutos = registroProdutos + 1
        cadastrarProduto(registroProdutos)
      elif opcao == 2:
        consultarProduto()
      elif opcao == 3:
        removerProduto()
      elif opcao == 4:
        print('Programa finalizado')
        break
      else:
        print('Digite somente uma das opções do MENU')
        continue    #mostrar mensagem de erro caso nescessario.
    except ValueError:
        print('Pare de digitar números invalidos!...')
