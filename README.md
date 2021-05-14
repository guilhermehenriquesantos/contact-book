# Agenda de contatos

![Python Badge](https://img.shields.io/badge/python-%5E3.9-blue?style=flat-square&logo=python&logoColor=white)

A tecnologia utilizadas está no shield acima.
## Instalação

Faça o clone desse repositório. Ele contém dois arquivos principais:

- agenda.py (código fonte do projeto em python)
- agenda.csv (base de dados fictícia - representa os contatos adicionados na agenda)

### agenda.csv

Representação dos contatos adicionados na agenda, já vem populado para que você possa ver como funciona todas as funções do programa. Ele é carregado quando se executa o programa **agenda.py** e recebe uma atualização a cada alteração feita no agenda.py, ao sair ele exporta novamente a agenda com os contatos atualizados para o arquivo CSV, composto pelas seguintes informações do contato:

- Nome;
- Telefone;
- E-mail;
- Endereço.

Foi utilizado um arquivo CSV pela sua compatibilidade com outros softwares, por exemplo, o Microsoft Excel, LibreOffice Calc e o Google Planilhas. 

### agenda.py

Código fonte da aplicação, para executá-lo basta dar o comando **python3.9 agenda.py** ou apenas executar um **run** na IDE de sua preferência para arquivos python.

A agenda é carregada do arquivo CSV **agenda.csv**, em que ele pode ou não existir:

- **Arquivo agenda.csv existe:** a agenda é carregada, os contatos são armazenados em uma estrutura de dados de dicionário, chamado AGENDA, por meio dele ocorre todas as alterações dentro da agenda.
- **Arquivo agenda.csv não existe:** a agenda não é carregada, entrando no fluxo de exceção que avisa ao usuário que a agenda está vazia e o mesmo precisa adicionar contatos para poder navegar pelas funções, os contatos são armazenados em uma estrutura de dados de dicionário (que inicialmente será vazio), chamado AGENDA, por meio dele ocorre todas as alterações dentro da agenda.

**Funções da agenda:**

- Mostrar todos os contatos;
- Adicionar um novo contato;
- Editar os dados de um contato existente;
- Buscar um contato existente;
- Excluir um contato;
- Exportar e importar contatos de um arquivo CSV;
- Sair do programa.

