from functions import Option
from contacts import contatos

while True:
    Option.clear()
    print("Bem vindo a sua agenda.")
    print("1. Ver contatos favoritos.")
    print("2. Ver contatos.")
    print("3. Novo contato.")
    print("4. Editar contato.")
    print("5. Alternar favorito.")
    print("6. Deletar contato.")

    try:
        escolha = int(input("\nSelecione a opção: "))
        Option.clear()
    except ValueError:
        print("Opção Invalida.")
        input()
        Option.clear()

    match escolha:
        case 1:
            print("Contatos Favoritos")
            Option.seeFavoriteContacts(contatos)
            input()
        case 2:
            print("Seus contatos\n")
            Option.seeContacts(contatos)
            input()
        case 3:
            print("Criar novo contato\n")
            contatos.append(Option.createContact())
            print("Contato criado com sucesso")
            input()
        case 4:
            Option.seeContacts(contatos)
            contactEdit = input("Editar qual contato:\n")
            Option.editContact(contatos, contactEdit)
            input()
        case 5:
            Option.seeContacts(contatos)
            contactFav = input("Alternar o favorito de:\n")
            Option.toggleFavorite(contatos, contactFav)
            input()
        case 6:
            Option.seeContacts(contatos)
            contactName = input("Deletar qual contato?\n")
            Option.deleteContact(contatos, contactName)
            input()
