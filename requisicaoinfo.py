import os
os.system ("cls")
from pycep_correios import get_address_from_cep, WebService

cadastro = {"Email": ""}

email = input("Digite seu email: ")

cadastro["Email"] = email

dados = {"Nome Completo": "",  "Telefone": "","Profissão": "", "Nacionalidade": "", "Data de Nascimento": "", "Gênero": "", "CPF": "", "RG": "", "Órgão Expedidor": "", "Endereço": ""}

nome_completo = input("Digite seu nome completo: ")
telefone = input("Digite seu telefone: ")
profissao = input("Digite sua profissão: ")
nacionalidade = input("Digite sua nacionalidade: ")
data_nascimento = input("Digite sua Data de Nascimento: ")
genero = input("Digite seu Gênero: ")
cpf = input("Digite seu CPF: ")
rg = input("Digite seu RG: ")
orgao_exp = input("Digite o Órgão Expedidor: ")
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
dados["Endereço"] = cep
endereco = get_address_from_cep(cep, webservice=WebService.CORREIOS)
endereco_comp={
    'Rua': endereco['logradouro'],
    'Numero': '',
    'Complemento': '',
    'Bairro': endereco['bairro'],
    'Cidade': endereco['cidade'],
    'Estado': endereco['uf'],
    'País': 'Brasil'
}

endereco_comp['Numero']= int(input("Digite o numero de sua residencia: "))
complemento = input("Endereço possue complemento? ").lower()
if complemento == 's':
    endereco_comp['Complemento']=input("Digite o complemento:")
elif complemento == 'n':
    endereco_comp.pop('Complemento', None)

for i in endereco_comp:
    print(f'{i}: {endereco_comp[i]}')
corrrecao =input('O endereço esta correto? ').lower()
if corrrecao == 'n':
    cep = input("Digite o CEP: ")
    endereco = get_address_from_cep(cep, webservice=WebService.CORREIOS)
    endereco_comp={
        'Rua': endereco['logradouro'],
        'Numero': '',
        'Complemento': '',
        'Bairro': endereco['bairro'],
        'Cidade': endereco['cidade'],
        'Estado': endereco['uf'],
        'País': 'Brasil'
    }

    endereco_comp['Numero']= int(input("Digite o numero de sua residencia: "))
    complemento = input("Endereço possue complemento? ").lower()
    if complemento == 's':
        endereco_comp['Complemento']=input("Digite o complemento:")
    elif complemento == 'n':
        endereco_comp.pop('Complemento', None)
    for i in endereco_comp:
        print(f'{i}: {endereco_comp[i]}')
cadastro['Endereço']=endereco_comp

print('\n')
for i in dados:
    if i == 'Endereço':
        for dado in endereco_comp:
            print(f'{dado}: {endereco_comp[dado]}')
    else:
        print(f'{i}: {dados[i]}')

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

print('\n')
for i in dados:
    if i == 'Endereço':
        for dado in endereco_comp:
            print(f'{dado}: {endereco_comp[dado]}')
    else:
        print(f'{i}: {dados[i]}')
