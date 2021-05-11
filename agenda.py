import os


AGENDA = {}


def mostrar_contato(contato):
    print('\nNome:', contato)
    print('Telefone:', AGENDA[contato]['telefone'])
    print('E-mail:', AGENDA[contato]['email'])
    print('Endereço:', AGENDA[contato]['endereco'])
    print('\n-------------------------------')


def mostrar_agenda():
    if len(AGENDA) > 0:
        for contato in AGENDA:
            mostrar_contato(contato)
    else:
        print('\nNenhum contato...\n')


def buscar_contatos():
    print('\nEscolha uma opção sobre a busca que você quer realizar:\n')
    print('1 - Nome')
    print('2 - Telefone')
    print('3 - E-mail')
    print('4 - Endereço\n')

    try:
        info = int(input('Digite o número que representa a forma na qual você quer buscar os contatos: '))

        if(info == 1):
            nome = input('\nDigite o nome que procura: ')
            for contato in AGENDA:
                if contato == nome:
                    mostrar_contato(contato)

        elif(info == 2):
            telefone = input('\nDigite o telefone que procura: ')
            for contato in AGENDA:
                if AGENDA[contato]['telefone'] == telefone:
                    mostrar_contato(contato)

        elif(info == 3):
            email = input('\nDigite o e-mail que procura: ')
            for contato in AGENDA:
                if AGENDA[contato]['email'] == email:
                    mostrar_contato(contato)

        elif(info == 4):
            endereco = input('\nDigite o e-mail que procura: ')
            for contato in AGENDA:
                if AGENDA[contato]['endereco'] == endereco:
                    mostrar_contato(contato)

    except Exception as error:
        print('\nEscolha uma opção válida\n')


def inserir_editar_contato(nome):
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o e-mail do contato: ')
    endereco = input('Digite o endereço do contato: ')

    incluir_contato(nome, telefone, email, endereco)
    print('\n>>>>> O contato {} foi adicionado/editado com sucesso! <<<<<\n'.format(nome))
    exportar_agenda()


def incluir_contato(nome, telefone, email, endereco):
    AGENDA[nome] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco
    }


def excluir_contato(nome):
    try:
        AGENDA.pop(nome)
        print('\n>>>>> O contato {} foi excluído com sucesso! <<<<<\n'.format(nome))
        exportar_agenda()
    except KeyError:
        print('\nContato inexistente!\n')


def exportar_agenda():
    try:
        with open('agenda.csv', 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write('{},{},{},{}\n'.format(contato, telefone, email, endereco))

            print("\n>>> Agenda exportada para o arquivo agenda.csv nessa mesma pasta! <<<\n")

    except Exception as error:
        print('\nAlgum erro ocorreu ao exportar a agenda\n')


def importar_agenda():
    try:
        with open('agenda.csv', 'r') as arquivo:
            contatos = arquivo.readlines()
            for contato in contatos:
                detalhes = contato.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_contato(nome, telefone, email, endereco)

    except FileNotFoundError as error:
        print('\n>>> Sua agenda de contatos está vazia, adicione contatos! <<<')
    except Exception as error:
        print('\nAlgum erro ocorreu ao importar a agenda\n')


def menu():
    print('\n##########################################################')
    print('################### AGENDA DE CONTATOS ###################')
    print('##########################################################\n')
    print('Olá, o que você deseja ? Escolha uma das opções abaixo:\n')
    print('1 - Mostrar todos os contatos')
    print('2 - Adicionar novo contato')
    print('3 - Editar os dados de um contato')
    print('4 - Buscar um contato existente')
    print('5 - Excluir contato')
    print('0 - Sair')


# MAIN #
if __name__=="__main__":

    importar_agenda()

    while True:

        try:
            menu()

            opcao = int(input('\nNúmero da opção escolhida: '))

            os.system('cls' if os.name == 'nt' else 'clear')

            if(opcao == 1):
                mostrar_agenda()

            elif(opcao == 2):
                nome = input('\nDigite o nome do novo contato: ')
                try: 
                    AGENDA[nome]
                    print('\nContato {} já existe na agenda!\n'.format(nome))
                except Exception as error:
                    
                    inserir_editar_contato(nome)

            elif(opcao == 3):
                nome = input('Edite o nome do contato: ')
                try:
                    AGENDA[nome]
                    print('\nEditando contato {}\n'.format(nome))
                    pass
                except Exception as error:
                    print('\nEsse contato ainda não foi adicionado...\n')
                    continue
                inserir_editar_contato(nome)

            elif(opcao == 4):
                buscar_contatos()

            elif(opcao == 5):
                nome = input('\nDigite o nome do contato que deseja excluir: ')
                excluir_contato(nome)

            elif(opcao == 0):
                print('\nFechando o programa!\n')
                break

            else:
                print('\nEscolha uma opção válida, fechando programa!\n')
                break

        except ValueError as error:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\nDigite um número* que representa a opção escolhida. Estamos encerrando o programa!\n')
            break

        except Exception as error:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Ocorreu um erro e temos que fechar o programa, desculpe!\n')
            break

    exportar_agenda()
