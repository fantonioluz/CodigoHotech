
lista_dados = []

dados = {"Nome": "", "Sobrenome": "", "CPF": "", "Endereço": "", "RG": ""}

nome = input("Digite o nome: ")
sobrenome = input("Digite o sobrenome: ")
cpf = input("Digite o CPF: ")
endereco = input("Digite o endereço: ")
rg = input("Digite o RG: ")

dados["Nome"] = nome
dados["Sobrenome"] = sobrenome
dados["CPF"] = cpf
dados["Endereço"] = endereco
dados["RG"] = rg

lista_dados.append(dados)

for dado in lista_dados:
    print(dado)

escolha = input("Deseja editar algum dado? ")

if escolha == "sim":
    item_editar = input("Qual item deseja editar? ")
    if item_editar == "nome":
        novo_nome = input("Digite o novo nome: ")
        dados["Nome"] = novo_nome
    elif item_editar == "sobrenome":
        novo_sobrenome = input("Digite o novo sobrenome: ")
        dados["Sobrenome"] = novo_sobrenome
    elif item_editar == "CPF":
        novo_CPF = input("Digite o novo CPF: ")
        dados["CPF"] = novo_CPF
    elif item_editar == "endereco":
        novo_endereco = input("Digite o novo endereço: ")
        dados["Endereço"] = novo_endereco
    elif item_editar == "RG":
        novo_RG = input("Digite o novo RG: ")
        dados["RG"] = novo_RG

for dado in lista_dados:
    print(dado)
