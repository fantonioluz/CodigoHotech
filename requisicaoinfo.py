import os
os.system ("cls")
import qrcode
import matplotlib
from pycep_correios import get_address_from_cep, WebService

cadastro = {"Email": "",'Senha': ''}#Parte onde seria realizado o cadastro do usuario para autenticação do site, podendo ser realizado por facebook e google tambem


dados = {"Nome Completo": "",  "Telefone": "","Profissão": "", "Nacionalidade": "", "Data de Nascimento": "", "Gênero": "", "CPF": "", "RG": "", "Órgão Expedidor": "", "Endereço": ""}

nome_completo = input("Digite seu nome completo: ")
telefone = input("Digite seu telefone: ")
profissao = input("Digite sua profissão: ")
nacionalidade = input("Digite sua nacionalidade: ")
data_nascimento = input("Digite sua Data de Nascimento: ")
genero = input("Digite seu Gênero: ")
cpf = input("Digite seu CPF: ")    
a = int(cpf) // 10000000000 % 10
b = int(cpf) // 1000000000 % 10
c = int(cpf) // 100000000 % 10
d = int(cpf) // 10000000 % 10
e = int(cpf) // 1000000 % 10
f = int(cpf) // 100000 % 10
g = int(cpf) // 10000 % 10
h = int(cpf) // 1000 % 10
i = int(cpf) // 100 % 10
j = int(cpf) // 10 % 10
k = int(cpf) // 1 % 10
verif_j = (10*a + 9*b + 8*c + 7*d + 6*e + 5*f + 4*g + 3*h + 2*i)*10
verif_k = (11*a + 10*b + 9*c + 8*d + 7*e + 6*f + 5*g + 4*h + 3*i + 2*j)*10
if a==b==c==d==e==f==g==h==i==j==k:
    print("O CPF informado não está correto")
    novo_cpf = input("Digite seu novo CPF: ")
    cpf = novo_cpf
if verif_j%11 == j and verif_k%11 == k:
        print('CPF correto')
else:
    print("O CPF informado não está correto")
    novo_cpf = input("Digite seu novo CPF: ")
    cpf = novo_cpf

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
brasil = input('Reside no Brasil? ').lower()
if brasil == 's':
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
    complemento = input("Endereço possui complemento? ").lower()
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
else:
    endereco_comp={
        'Rua': '',
        'Numero': '',
        'Cidade': '',
        'Estado': '',
        'País': ''
    }
    endereco_comp['Rua']=input('Digite a rua: ')
    endereco_comp['Numero']=input('Digite o numero: ')
    endereco_comp['Cidade']=input('Digite a cidade: ')
    endereco_comp['Estado']=input('Digite o estado: ')
    endereco_comp['País']=input('Digite o país: ')

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


arquivo = open(dados['Nome Completo']+'.txt', 'w', encoding='utf8')
for i in dados:
    if i == 'Endereço':
        for dado in endereco_comp:
            arquivo.write(f'{dado}: {endereco_comp[dado]}\n')
    else:
        arquivo.write(f'{i}: {dados[i]}')
        arquivo.write('\n')
arquivo.close()
print('\n')
for i in dados:
    if i == 'Endereço':
        for dado in endereco_comp:
            print(f'{dado}: {endereco_comp[dado]}')
    else:
        print(f'{i}: {dados[i]}')

data = "https://linktr.ee/coxinhaCESAR"
qr = qrcode.QRCode(version = 1, 
                   box_size = 10, 
                   border = 5) 
qr.add_data(data) 
  
qr.make(fit = True) 
img = qr.make_image(fill_color = '#51CE94', 
                    back_color = 'white') 
  
img.save(dados['Nome Completo']+' codigo acesso.png')
