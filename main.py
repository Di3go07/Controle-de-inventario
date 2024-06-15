import getpass
import csv
from csv import writer 
import pandas as pd

#BANCO DE DADOS
data = pd.read_csv(r'./tabela_users.csv', sep=',')
#abre o banco de dados


#FUNÇÕES

#criando usuarios
cargos = ['gerente','administrador','funcionario','cliente']
def criar_usuarios():
    print('-'*50)
    criar_id = int(input('Digite um id: '))
    criar_user = str(input('Nome do usuário: '))
    criar_senha = str(input('Senha: '))
    confirmar_senha = str(input('Confirme a senha: '))
    if criar_senha == confirmar_senha:
        criar_cargo = str(input('Qual o cargo do usuário: '))
        if criar_cargo in cargos:
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
        print('Senhas não coincidem, tente novamente...')
        retomada = criar_usuarios()

#página login usuários
def login_user():
    print('-'*50)
    with open('./tabela_users.csv', 'a') as f_object: 
        user_atual = input('Usuario: ')
        senha_atual = input('Senha: ')
        verficacao = verificar_usuarios(user_atual, senha_atual)
        quebra = usuario_linha(user_atual)
    f_object.close() 

#verificando usuarios
def verificar_usuarios(user, senha):
    with open('./tabela_users.csv', 'a') as f_object: 
        if user in data['nomes'].values and senha in data['senhas'].values:
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
    print('-'*50)
    quebra = data['nomes'] == user
    linha_user = data[quebra]

    #gerente
    if linha_user['cargos'].unique() == 'gerente':
        print('1 - arquivos')
        print('2 - usuarios')
        resposta = int(input('O que você deseja manipular: '))
        if resposta == 1:
            print('1 - Ler arquivo')
            print('2 - Editar arquivo')
            print('3 - Adicionar arquivo')
            print('4 - Excluir arquivo')
            arq_resposta = int(input('Opção: '))
        elif resposta == 2:
            print('1 - Tabela usuarios')
            print('2 - Adicionar usuario')
            print('3 - Excluir usuario')
            usr_resposta = int(input('Opção: '))

    #administrador
    elif linha_user['cargos'].unique() == 'administrador':
            print('1 - Ler arquivo')
            print('2 - Editar arquivo')
            print('3 - Adicionar arquivo')
            arq_resposta = int(input('Opção: '))

    #funcionario
    elif linha_user['cargos'].unique() == 'funcionario':
            print('1 - Ler arquivo')
            print('2 - Adicionar arquivo')
            arq_resposta = int(input('Opção: '))

    #cliente
    else:
        print(data) #PRECISA MUDAR DEPOIS

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

