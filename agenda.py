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


def mostrar_agenda():
    for contato in AGENDA:
        mostrar_contato(contato)


def mostrar_contato(contato):
    print("\nNome:", contato)
    print("Telefone:", AGENDA[contato]["telefone"])
    print("E-mail:", AGENDA[contato]["email"])
    print("Endereço:", AGENDA[contato]["endereco"])
    print("\n-------------------------------")


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

buscar_contatos()