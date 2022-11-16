import os
os.system ("cls")
# Import das bibliotecas necessarias
  # Gerador do QR Code
import qrcode
  # Get de enderecos via CEP
from pycep_correios import get_address_from_cep, WebService

# ////////////////////// Inicio do Codigo //////////////////////

# ////////////////////// Inicio da parte de Inputs //////////////////////

  # Onde sera realizado o cadastro do usuario para autenticação do site, podendo ser realizado por facebook e google tambem
cadastro = {"Email": "",'Senha': ''}

  # Dicionario para salvar os dados do usuario
dados = {"Nome Completo": "",  "Telefone": "","Profissão": "", "Nacionalidade": "", "Data de Nascimento": "", "Gênero": "", "CPF": "", "RG": "", "Órgão Expedidor": "", "Endereço": ""}

# Inputs
  # Obtencao dos dados necessarios para o checkin
nome_completo = input("Digite seu nome completo: ")
telefone = input("Digite seu telefone: ")
profissao = input("Digite sua profissão: ")
nacionalidade = input("Digite sua nacionalidade: ")
data_nascimento = input("Digite sua Data de Nascimento: ")
genero = input("Digite seu Gênero: ")
cpf = input("Digite seu CPF: ")    
  # Verificacao de CPF (Verifica cada digito do CPF)
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
  # Formula para verificacao do CPF
verif_j = (10*a + 9*b + 8*c + 7*d + 6*e + 5*f + 4*g + 3*h + 2*i)*10
verif_k = (11*a + 10*b + 9*c + 8*d + 7*e + 6*f + 5*g + 4*h + 3*i + 2*j)*10
  # Se todos os digitos forem iguais, informa que o CPf esta incorreto e pede para digitar novamente
if a==b==c==d==e==f==g==h==i==j==k:
    print("O CPF informado não está correto")
    novo_cpf = input("Digite seu novo CPF: ")
    cpf = novo_cpf
  # Verifica a formula, caso nao ocorra erro, o CPF esta correto. Caso, sim ele informa que esta incorreto
  # E pede para digitar novamente um novo CPF
if verif_j%11 == j and verif_k%11 == k:
        print('CPF correto')
else:
    print("O CPF informado não está correto")
    novo_cpf = input("Digite seu novo CPF: ")
    cpf = novo_cpf
  # Continuacao dos Inputs de cadastro
rg = input("Digite seu RG: ")
orgao_exp = input("Digite o Órgão Expedidor: ")
brasil = input('Reside no Brasil? ').lower()

  # Adiciona ao dicionario "dados" as informacoes do usuario
dados["Nome Completo"] = nome_completo
dados["Telefone"] = telefone
dados["Profissão"] = profissao
dados["Nacionalidade"] = nacionalidade
dados["Data de Nascimento"] = data_nascimento
dados["Gênero"] = genero
dados["CPF"] = cpf
dados["RG"] = rg
dados["Órgão Expedidor"] = orgao_exp
  # Se o pais for Brasil, ele pede o CEP e utiliza a biblioteca do correios para pegar o endereco completo do usuario
if brasil == 's':
    cep = input("Digite o CEP: ")
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
  # Pede o numero da residencia e pergunta se possui complemento do mesmo
    endereco_comp['Numero']= int(input("Digite o numero de sua residencia: "))
    complemento = input("Endereço possui complemento? ").lower()
    if complemento == 's':
        endereco_comp['Complemento']=input("Digite o complemento:")
    elif complemento == 'n':
        endereco_comp.pop('Complemento', None)
  # Print do endereco completo e pergunta ao usuario se o endereco esta correto
    for i in endereco_comp:
        print(f'{i}: {endereco_comp[i]}')
    corrrecao =input('O endereço esta correto? ').lower()
  # Se o endereco nao estiver correto, o usuario tem a opcao de informar novamente e corrigir o mesmo
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
  # Repeticao das perguntas de endereco
        endereco_comp['Numero']= int(input("Digite o numero de sua residencia: "))
        complemento = input("Endereço possue complemento? ").lower()
        if complemento == 's':
            endereco_comp['Complemento']=input("Digite o complemento:")
        elif complemento == 'n':
            endereco_comp.pop('Complemento', None)
        for i in endereco_comp:
            print(f'{i}: {endereco_comp[i]}')
    cadastro['Endereço']=endereco_comp
  # Caso nao resida no brasil ele pergunta o endereco internacional
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
  # Print de toda a informacao coletada do usuario ate o momento
print('\n')
for i in dados:
   if i == 'Endereço':
       for dado in endereco_comp:
           print(f'{dado}: {endereco_comp[dado]}')
   else:
       print(f'{i}: {dados[i]}')
  # Pergunta se o usuario deseja editar algum dado
escolha = input("Deseja editar algum dado? ").lower()
  # Se sim, pergunta qual dado deseja editar e faz um novo input para o usuario
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
# ////////////////////// Fim da parte de Inputs //////////////////////

# ////////////////////// Inicio da parte de criacao de documentos //////////////////////

  # Criacao de um arquivo TXT com o nome do usuario e todos os dados coletados
arquivo = open(dados['Nome Completo']+'.txt', 'w', encoding='utf8')
for i in dados:
    if i == 'Endereço':
        for dado in endereco_comp:
            arquivo.write(f'{dado}: {endereco_comp[dado]}\n')
    else:
        arquivo.write(f'{i}: {dados[i]}')
        arquivo.write('\n')
arquivo.close()
# ////////////////////// Fim da parte de criacao de documentos //////////////////////
print('\n')
  # Print dos dados do usuario no console
for i in dados:
    if i == 'Endereço':
        for dado in endereco_comp:
            print(f'{dado}: {endereco_comp[dado]}')
    else:
        print(f'{i}: {dados[i]}')
# ////////////////////// Inicio da criacao do QR Code //////////////////////

  # Criacao do QR Code
   #  Redireciona para um link especifico no sistema da Hotech
data = "https://linktr.ee/coxinhaCESAR"
  # Definicao do tamanho da foto do QR Code
qr = qrcode.QRCode(version = 1, 
                   box_size = 10, 
                   border = 5) 
  # Adiciona o Link fornecido ao QR Code
qr.add_data(data) 
  #  Metodo ".make" define que o tamanho do QR Code ira ser do tamanho defino previamente
qr.make(fit = True) 
  # Definindo as cores do QR Code
img = qr.make_image(fill_color = '#51CE94', 
                    back_color = 'white') 
  # Salva em uma arquivo tipo ".png" o QR Code
img.save(dados['Nome Completo']+' codigo acesso.png')
# ////////////////////// Fim da criacao do QR Code //////////////////////
# ////////////////////// Fim do Codigo //////////////////////
