# Programa para inventário 

## 🛠️ Apresentação
O meu grupo do projeto do curso Desenvolve Itabira ficou responsável pela empresa FeP Reparos e Reformas. Tendo em vista as necessidades e organização do nosso cliente, o grupo propos criar um programa em Python
em que ele possa controlar o inventário de forma prática e fácil, contendo diferentes níveis de usuários e uma tabela com seus materiais.

## ⚙️ Estrutura
Como dito, o programa possui diferentes níveis de usuários, os cargos, com funções diferentes e um banco de dados onde pode-se acessar e alterar o inventário da empresa e os usuários cadastrados

**💼 CARGOS** <br>
A habilidade de cada cargo <br>
<br> Gerente
* Cargo mais alto
* Excluir produtos e usuários
* Adicionar produtos e usários
* Editar arquivos
* Ler arquivos

Administrador
* Ler arquivos
* Adicionar produtos e usuários
* Editar arquivos

Funcionario
* Ler arquivos
* Adicionar produtos

Cliente
* Ler tabela de produtos


**💾 BANCO DE DADOS**  
Para o programa, foram utilizados os seguintes arquivos do banco de dados:
* tabela_produtos.csv - cada linha armazena informações sobre um produto, sendo elas: id, material, preço por unidade e quantidade
* tabela_users.csv - cada linha armazena informações sobre um usuário do sistema, sendo elas: id, nome, senha e cargo

## 📋 Pré-requisitos 
Do que você precisa antes de abrir o código:

Python

Baixar o pandas:
```
pip install pandas
```
Baixar o repositorio:
```
Trabalho_Pratico
```

## 🚨 Avisos
Alguns cuidados a serem tomados ao utilizar o programa:
* Não utilize acentos ao preenchcer os campos de imput
* Letra maiscula é diferente de letra minuscula
* Plural é diferente de singular

## 🏁 Começando
Como usar o programa

Depois do dowload do repositório, abra:
```
Trabalho_Pratico/main.py
```

Dentro do arquivo, inicie o terminal

No terminal, escolha entre logar com um usuario ou criar um novo usuário

Caso deseje logar com um usuario, algumas contas já criadas são:
| id           | nome           | senha         | cargo         |
| :---         | :---           | :---          | :---          |
| 1            | gerente        | 23901         | gerente       |
| 2            | administrador  | 23901         | administrador |
| 3            | funcionario    | 23901         | funcionario   |
| 4            | cliente        | 23901         | cliente       |

Aproveite o programa!

## 👨‍💻 Desenvolvedores

Diego Penna Andrade Barros <br>
PDITA 274

Thiago Santos Madeira <br>
PDITA 010

Maria Clara Souza Araújo <br>
199
