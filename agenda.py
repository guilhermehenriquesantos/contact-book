AGENDA = {}

AGENDA['Guilherme Henrique'] = {
    "telefone":"(34)99999-9999",
    "email":"guilherme@teste.com",
    "endereco":"Av. Brasil"
}

AGENDA['Josefina Pires'] = {
    "telefone":"(34)98888-8888",
    "email":"josefina@teste.com",
    "endereco":"Av. Pássaros"
}


def mostrar_contato(contato):
    print("\nNome:", contato)
    print("Telefone:", AGENDA[contato]["telefone"])
    print("E-mail:", AGENDA[contato]["email"])
    print("Endereço:", AGENDA[contato]["endereco"])
    print("\n-------------------------------")


def mostrar_agenda():
    for contato in AGENDA:
        mostrar_contato(contato)


def buscar_contatos():
    print("\nEscolha uma opção sobre a busca que você quer realizar:\n")
    print("1 - Nome")
    print("2 - Telefone")
    print("3 - E-mail")
    print("4 - Endereço\n")
    info = input("Digite o número que representa a forma na qual você quer buscar os contatos: ")

    if(info == "1" or info == "Nome" or info == "nome"):
        nome = input("\nDigite o nome que procura: ")
        for contato in AGENDA:
            if contato == nome:
                mostrar_contato(contato)
    elif(info == "2" or info == "Telefone" or info == "telefone"):
        telefone = input("\nDigite o telefone que procura: ")
        for contato in AGENDA:
            if AGENDA[contato]["telefone"] == telefone:
                mostrar_contato(contato)
    elif(info == "3" or info == "E-mail" or info == "e-mail" or info == "email" or info == "Email"):
        email = input("\nDigite o e-mail que procura: ")
        for contato in AGENDA:
            if AGENDA[contato]["email"] == email:
                mostrar_contato(contato)
    elif(info == "4" or info == "Endereço" or info == "endereço" or info == "Endereco" or info == "endereco"):
        endereco = input("\nDigite o e-mail que procura: ")
        for contato in AGENDA:
            if AGENDA[contato]["endereco"] == endereco:
                mostrar_contato(contato)
    else:
        print("Escolha uma opção válida")


def inserir_editar_contato(nome, telefone, email, endereco):
    AGENDA[nome] = {
        "telefone": telefone,
        "email": email,
        "endereco": endereco
    }
    print("\n>>>>> O contato {} foi adicionado/editado com sucesso! <<<<<\n".format(nome))


def excluir_contato(nome):
    AGENDA.pop(nome, None)
    print("\n>>>>> O contato {} foi excluído com sucesso! <<<<<\n".format(nome))


def menu():
    print("\n##########################################################")
    print("################### AGENDA DE CONTATOS ###################")
    print("##########################################################\n")
    print("Olá, o que você deseja ? Escolha uma das opções abaixo:\n")
    print("1 - Mostrar todos os contatos")
    print("2 - Adicionar novo contato")
    print("3 - Buscar um contato existente")
    print("4 - Editar os dados de um contato")
    print("5 - Excluir contato")
    print("6 - Sair")
    opcao = input("\nNúmero da pção escolhida: ")

    if(opcao == "1"):
        mostrar_agenda()
    elif(opcao == "2"):
        nome = input("\nDigite um nome para o novo contato: ")
        telefone = input("Digite um telefone para o novo contato: ")
        email = input("Digite um e-mail para o novo contato: ")
        endereco = input("Digite um endereço para o novo contato: ")
        inserir_editar_contato(nome, telefone, email, endereco)
    elif(opcao == "3"):
        buscar_contatos()
    elif(opcao == "4"):
        nome = input("\nDigite o nome do contato existente: ")
        telefone = input("Novo número para {}: ".format(nome))
        email = input("Novo e-mail para {}: ".format(nome))
        endereco = input("Novo endereço para {}: ".format(nome))
        inserir_editar_contato(nome, telefone, email, endereco)
    elif(opcao == "5"):
        nome = input("\nDigite o nome do contato que deseja excluir: ")
        excluir_contato(nome)
    elif(opcao == "6"):
        exit()
    else:
        print("\n-> Escolha uma opção válida <-\n")


# MAIN #
menu()