import os



class Option:

    def clear():
        os.system("clear")

    def createContact():
        contactName = input("Nome do contato: ")
        os.system("clear")
        contactNumber = input("Numero do contato: ")
        os.system("clear")
        contactEmail = input("Email do contato: ")
        os.system("clear")
        isFavorite = input("Salvar como favorito?\nSe sim digite 1: ")
        if isFavorite == "1":
            favorite = True
        else:
            favorite = False

        contact = {
            "Nome": contactName,
            "Numero": contactNumber,
            "Email": contactEmail,
            "Favoritos": favorite
        }

        return contact

    def seeContacts(list):
        for index, value in enumerate(list, start=1):
            print(index)
            print(f'Nome:{value["Nome"]}')
            print(f'Número:{value["Numero"]}')
            print(f'Email:{value["Email"]}')
            if list[index-1]["Favoritos"] == True:
                print("★")
            print('----------------------------------------')

    def seeFavoriteContacts(list):
        for index, value in enumerate(list, start=1):
            if list[index-1]["Favoritos"] == True:
                print(index)
                print(f'Nome:{value["Nome"]}')
                print(f'Número:{value["Numero"]}')
                print(f'Email:{value["Email"]}')
                print('----------------------------------------')

    def deleteContact(list, number):
        try:
            print(f'{list[int(number)-1]["Nome"]} foi deletado.')
            del list[int(number)-1]
        except:
            print("Valor Invalido")

    def toggleFavorite(list, number):
        try:
            index = int(number)-1
        except:
            print("Contato não existe")
        if list[index]["Favoritos"] == True:
            list[index]["Favoritos"] = False
            print(f'{list[index]["Nome"]} foi desmarcado como favorito')
        else:
            list[index]["Favoritos"] = True
            print(f'{list[index]["Nome"]} foi marcado como favorito')

    def editContact(list, number):
        try:
            index = int(number) - 1
        except:
            print("Opção Invalida")
            input()
            return
        newName = input('Editar nome: ')
        newNumber = input('Editar numero: ')
        newEmail = input('Editar Email: ')
        if newName:
            list[index]["Nome"] = newName
        if newNumber:
            list[index]["Número"] = newNumber
        if newEmail:
            list[index]["Email"] = newEmail
        pass
