import getpass
import csv
from csv import writer 
import pandas as pd

#BANCO DE DADOS
data = pd.read_csv(r'./tabela_users.csv', sep=',')
data_prod = pd.read_csv(r'./tabela_produtos.csv', sep=',')
#abre o banco de dados


#FUNÇÕES

#página login usuários
def login_user():
    print('-'*50)
    with open('./tabela_users.csv', 'a') as f_object: 
        user_atual = input('Usuario: ')
        senha_atual = getpass.getpass('Senha: ') #a senha não aparece ao ser digitada
        verficacao = verificar_usuarios(user_atual, senha_atual)
        quebra = usuario_linha(user_atual)
    f_object.close() 

#verificando usuarios
def verificar_usuarios(user, senha):
    with open('./tabela_users.csv', 'a') as f_object: 
        if user in data['nomes'].values and senha in data['senha'].values:
            print('Bem vindo!')
        else:
            print('Usuário não encontrado')
            redirecao = input('Deseja criar um usuário [Y/n]: ')
            if redirecao == 'Y':
                retomada = criar_usuarios()
            else:
                retomada = login_user()
    f_object.close()     

#página de habilidades dos usuários

def usuario_linha(user):
    global data
    print('-'*50)
    quebra = data['nomes'] == user
    linha_user = data[quebra]

    #gerente
    if linha_user['cargo'].unique() == 'gerente':
        print('Acessando como gerente')
        print('1 - inventários')
        print('2 - usuarios')
        resposta = int(input('O que você deseja manipular: '))
        if resposta == 1:
            print('1 - Ler inventário')
            print('2 - Editar produto')
            print('3 - Adicionar produto')
            print('4 - Excluir produto')
            gerente_resposta = int(input('Opção: '))
            if gerente_resposta == 1:
                print('Tabela produtos')
                print(data_prod) 
            if gerente_resposta == 3:
                sequencia = criar_produto()
            if gerente_resposta == 4:
                sequencia = del_prods()
        elif resposta == 2:
            print('1 - Tabela usuarios')
            print('2 - Adicionar usuario')
            print('3 - Excluir usuario')
            gerente_resposta = int(input('Opção: '))
            if gerente_resposta == 1:
                print(data)
                sequencia = usuario_linha(user)
            if gerente_resposta == 2:
                sequencia = criar_usuarios()
            if gerente_resposta == 3:
                sequencia = del_user()

    #administrador
    elif linha_user['cargo'].unique() == 'administrador':
            print('Acessando como administrador')
            print('1 - Ler inventário')
            print('2 - Editar produto')
            print('3 - Adicionar produto')
            print('4 - Tabela usuarios')
            adm_resposta = int(input('Opção: '))

    #funcionario
    elif linha_user['cargo'].unique() == 'funcionario':
            print('Acessando como funcionario')
            print('1 - Ler inventário')
            print('2 - Adicionar produto')
            func_resposta = int(input('Opção: '))

    #cliente
    elif linha_user['cargo'].unique() == 'cliente':
        print('Acessando como cliente')
        print('Tabela produtos')
        print(data_prod) 

#habilidades dos usuários

#criar usuarios
cargo = ['gerente','administrador','funcionario','cliente']
def criar_usuarios():
    print('-'*50)
    criar_id = int(input('Digite um id: '))
    criar_user = str(input('Nome do usuário: '))
    criar_senha = str(input('Senha: '))
    confirmar_senha = str(input('Confirme a senha: '))
    if criar_senha == confirmar_senha:
        criar_cargo = str(input('Qual o cargo do usuário: '))
        if criar_cargo in cargo:
            nv_user = [criar_id, criar_user, confirmar_senha, criar_cargo]
            with open('./tabela_users.csv', 'a') as f_object: 
                writer_object = writer(f_object) 
                writer_object.writerow(nv_user) 
            f_object.close() 
            print('Usuario cadastrado!')
            print('Abra novamente o programa')
        else:
            print('Cargo não existe!')
            print('Opções: gerente, administrador, funcionario e cliente')
            retomada = criar_usuarios()
    else:
        print('senha não coincidem, tente novamente...')
        retomada = criar_usuarios()

#excluir usuário
def del_user():
    print('Deletar usuário')
    del_id = int(input('Id: '))
    del_user = input('Usuário: ')
    global data
    with open('./tabela_users.csv', 'r') as file:
        reader = csv.reader(file)
        linhas = list(reader)
    linhas_filtradas = [linha for linha in linhas if len(linha) > 1 and linha[0] != del_id and linha[1] != del_user]
    with open('./tabela_users.csv', 'w', newline='') as file: 
        writer = csv.writer(file)
        writer.writerows(linhas_filtradas)
        print('Usuário excluido!')
        print('Abra novamente o programa')

#criar produto
def criar_produto():
    parar = False
    produto_id = int(input('Digite um id: '))
    produto_nome = str(input('Material: '))
    produto_preco = float(input('Preço por unidade: '))
    produto_quant = int(input('Quantidade: '))
    with open('./tabela_produtos.csv', 'r') as file:
        reader = csv.reader(file)
        linhas = list(reader)
        for linha in linhas:
            if len(linha) > 1 and linha[1].lower() == produto_nome.lower():
                print('Produto já foi adicionado')
                parar = True
    if parar != True:
        with open('./tabela_produtos.csv', 'a') as f_object: 
            nv_produto = [produto_id, produto_nome, produto_preco, produto_quant]
            writer_object = writer(f_object) 
            writer_object.writerow(nv_produto) 
            f_object.close() 
            print('Produto adicionado!')
            print('Abra novamente o programa')
    elif parar == True:
        ver_tabela = input('Deseja consultar a tabela [Y/n]: ')
        if ver_tabela == 'Y':
            print('Tabela produtos')
            print(data_prod) 
        elif ver_tabela == 'n':
            print('Fim')

#excluir produto
def del_prods():
    parar = False
    produtos = []
    print('Deletar produto')
    del_id = int(input('Id: '))
    del_prod = input('Produto: ')
    global data
    with open('./tabela_produtos.csv', 'r') as file:
        reader = csv.reader(file)
        linhas = list(reader)
        for lista in linhas:
            if len(lista) > 1:
                produtos.append(lista[1])
    if del_prod not in produtos:
        parar = True
    if parar != True:
        linhas_filtradas = [linha for linha in linhas if len(linha) > 1 and linha[0] != del_id and linha[1].lower() != del_prod.lower()]
        with open('./tabela_produtos.csv', 'w', newline='') as file: 
            writer = csv.writer(file)
            writer.writerows(linhas_filtradas)
            print('Produto excluido!')
            print('Abra novamente o programa')
    elif parar == True:
        print('Produto não encontrado')
        ver_tabela = input('Deseja consultar a tabela [Y/n]: ')
        if ver_tabela == 'Y':
            print('Tabela produtos')
            print(data_prod) 
        elif ver_tabela == 'n':
            print('Fim')


#HEADER
print('')
print('FeP REPAROS E REFORMAS')
print('Gerenciamento de inventários')
print('-'*50)

#INICO
print('BEM VINDO!')
print("1 - login")
print("2 - criar usuario")
inicio_resp = int(input('Sua escolha: '))
if inicio_resp == 1:
    retomada = login_user()
elif inicio_resp == 2:
    retomada = criar_usuarios()
else:
    print('valor inválido')

