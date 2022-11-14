import os
os.system ("cls")

lista_cadastro = []
lista_dados = []

cadastro = {"Email": ""}

email = input("Digite seu email: ")

cadastro["Email"] = email

dados = {"Nome Completo": "",  "Telefone": "","Profissão": "", "Nacionalidade": "", "Data de Nascimento": "", "Gênero": "", "CPF": "", "RG": "", "Órgão Expedidor": "", "CEP": ""}

nome_completo = input("Digite seu nome completo: ")
telefone = input("Digite seu telefone: ")
profissao = input("Digite sua profissão: ")
nacionalidade = input("Digite sua nacionalidade: ")
data_nascimento = input("Digite sua Data de Nascimento: ")
genero = input("Digite seu Gênero: ")
cpf = input("Digite seu CPF: ")
rg = input("Digite seu RG: ")
orgao_exp = input("Digite o Órgão Expedidor")
cep = input("Digite o CEP: ")

dados["Nome Completo"] = nome_completo
dados["Telefone"] = telefone
dados["Profissão"] = profissao
dados["Nacionalidade"] = nacionalidade
dados["Data de Nascimento"] = data_nascimento
dados["Gênero"] = genero
dados["CPF"] = cpf
dados["RG"] = rg
dados["Órgão Expedidor"] = orgao_exp
dados["CEP"] = cep

lista_cadastro.append(cadastro)

for cadastro in lista_cadastro:
    print(cadastro)

lista_dados.append(dados)

for dado in lista_dados:
    print(dado)

escolha = input("Deseja editar algum dado? ")

if escolha == "sim":
    item_editar = input("Qual item deseja editar? ")
    if item_editar == "email":
        novo_email = input("Digite o novo email: ")
        cadastro["Email"] = novo_email
    elif item_editar == "nome":
        novo_nome = input("Digite o novo nome: ")
        dados["Nome Completo"] = novo_nome
    elif item_editar == "telefone":
        novo_telefone = input("Digite o novo telefone: ")
        dados["Telefone"] = novo_telefone
    elif item_editar == "profissão":
        nova_profissao = input("Digite a nova profissão: ")
        dados["Profissão"] = nova_profissao
    elif item_editar == "nacionalidade":
        nova_nacionalidade = input("Digite o nova nacionalidade: ")
        dados["Nacionalidade"] = nova_nacionalidade
    elif item_editar == "data de nascimento":
        nova_data_nascimento = input("Digite a nova data de nascimento: ")
        dados["Data de Nascimento"] = nova_data_nascimento
    elif item_editar == "genero":
        novo_genero = input("Digite o novo gênero ")
        dados["Gênero"] = novo_genero
    elif item_editar == "CPF":
        novo_CPF = input("Digite o novo CPF: ")
        dados["CPF"] = novo_CPF
    elif item_editar == "RG":
        novo_RG = input("Digite o novo RG: ")
        dados["RG"] = novo_RG
    elif item_editar == "orgao expedidor":
        novo_orgao_exp = input("Digite o novo Órgão expedidor: ")
        dados["Órgão Expedidor"] = novo_orgao_exp
    elif item_editar == "cep":
        novo_cep = input("Digite o novo CEP: ")
        dados["CEP"] = novo_cep

for cadastro in lista_cadastro:
    print(cadastro)

for dado in lista_dados:
    print(dado)
