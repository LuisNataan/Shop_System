import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
cart = []
class main:
    def putcard(self, product, user, cart):
        print(f"{bcolors.BOLD}Insida os dados do seu cartão:{bcolors.ENDC}")
        number = input("Numero: ")
        cvv = input("cvv: ")
        date = input("Data: ")
        if number == "":
            print(f"{bcolors.FAIL}Você precisa inserir o numero do cartão!{bcolors.ENDC}")
            main.putcard(self, product, user, cart)
        if cvv == "":
            print(f"{bcolors.FAIL}Você precisa inserir o numero do cvv!{bcolors.ENDC}")
            main.putcard(self, product, user, cart)
        if date == "":
            print(f"{bcolors.FAIL}Você precisa inserir o numero de vencimento do cartão!{bcolors.ENDC}")
            main.putcard(self, product, user, cart)

        from Controller import CardController
        card = CardController.cardcontrol().get_by_number(number, "Model/Cards.txt")
        print(card)
        if card == []:
            print(f"{bcolors.FAIL} O cartão que você inseriu não existe!{bcolors.ENDC}")
            main.putcard(self, product, user, cart)

        if not card['cvv'] == cvv and not card['date'] == date:
            print(f"{bcolors.FAIL} Os dados do cartão que você inseriu não estão corretos!{bcolors.ENDC}")
            main.putcard(self, product, user, cart)

        from Controller import ProductController
        ProductController.ProductController().buy(cart, user, card)
    def showuserproducts(self, user, category):
        from Controller import ProductController
        print(f"{bcolors.BOLD}Selecione um produto:")
        from Controller import ProductController
        products = ProductController.ProductController().get_products("Model/Products.txt")
        for i in range(len(products)):
            if products[i]['category'] == str(category):
                print(f"{i+1} - {products[i]['name']} - {bcolors.OKGREEN}R${products[i]['price']}{bcolors.ENDC}")
        print("0 - Sair")
        print(f"{bcolors.WARNING} EXISTEM {random.randint(1000000, 9999999999999999999999)} USUARIOS INTERESSADOS NO PRODUTO QUE VOCÊ ESTÁ VENDO AGORA!{bcolors.ENDC}")
        print(f"{bcolors.WARNING} !!!!50% OFF!!!! VOCÊ TEM 5 SEGUNDOS PARA APROVEITAR A PROMOÇÃO EXCLUSIVA!{bcolors.ENDC}")

        product = input("")
        try:
            product = int(product)
        except:
            main.showuserproducts(self, user, category)
        if not product >= 1 and not product <= len(products):
            print(f"{bcolors.WARNING}Selecione um produto válido!{bcolors.ENDC}")
            main.showusercategorys()
        product = products[product - 1]
        global cart
        cart.append(product)
        another = input("Continuar Comprando: ")
        if another.lower() == "sim" or another.lower() == "sin" or another.lower() == "si" or another.lower() == "s" or another.lower() == "yes":
            main.showusercategorys(self, user)

        main.putcard(self, product, user, cart)
    def showusercategorys(self, user):
        print(f"{bcolors.BOLD}Selecione uma categoria:")
        from Controller import CategoryController
        categorys = CategoryController.CategoryController().get_categories("Model/Category.txt")
        for i in range(len(categorys)):
            print(f"{i+1} - {categorys[i]['name']}")
        print("0 - Sair")

        category = input("")

        try:
            category = int(category)
        except:
            main.showusercategorys(self, user)
        if not category >= 1 and not category <= len(categorys):
            print(f"{bcolors.WARNING}Selecione um produto válido!")
            main.showusercategorys(self, user)

        category = categorys[category-1]["id"]
        print("Categoria: " + category)
        main.showuserproducts(self, user, category)

    def showuserhome(self, user):
        print("-" * 187)
        print(("\t" * 10) + f"{bcolors.OKCYAN} __        ______      _____   ______          ______   __    __  __        ______  __    __  ________ {bcolors.ENDC}")
        print(("\t" * 10) + f"{bcolors.OKCYAN}|  \      /      \    |     \ /      \        /      \ |  \  |  \|  \      |      \|  \  |  \|        \ {bcolors.ENDC}")
        print(("\t" * 10) + f"{bcolors.OKCYAN}| $$     |  $$$$$$\    \$$$$$|  $$$$$$\      |  $$$$$$\| $$\ | $$| $$       \$$$$$$| $$\ | $$| $$$$$$$${bcolors.ENDC}")
        print(("\t" * 10) + f"{bcolors.OKCYAN}| $$     | $$  | $$      | $$| $$__| $$      | $$  | $$| $$$\| $$| $$        | $$  | $$$\| $$| $$__    {bcolors.ENDC}")
        print(("\t" * 10) + f"{bcolors.OKCYAN}| $$     | $$  | $$ __   | $$| $$    $$      | $$  | $$| $$$$\ $$| $$        | $$  | $$$$\ $$| $$  \   {bcolors.ENDC}")
        print(("\t" * 10) + f"{bcolors.OKCYAN}| $$     | $$  | $$|  \  | $$| $$$$$$$$      | $$  | $$| $$\$$ $$| $$        | $$  | $$\$$ $$| $$$$$   {bcolors.ENDC}")
        print(("\t" * 10) + f"{bcolors.OKCYAN}| $$_____| $$__/ $$| $$__| $$| $$  | $$      | $$__/ $$| $$ \$$$$| $$_____  _| $$_ | $$ \$$$$| $$_____ {bcolors.ENDC}")
        print(("\t" * 10) + f"{bcolors.OKCYAN}| $$     \ $$    $$ \$$    $$| $$  | $$       \$$    $$| $$  \$$$| $$     \|   $$ \| $$  \$$$| $$     \ {bcolors.ENDC}")
        print(("\t" * 10) + f"{bcolors.OKCYAN} \$$$$$$$$ \$$$$$$   \$$$$$$  \$$   \$$        \$$$$$$  \$$   \$$ \$$$$$$$$ \$$$$$$ \$$   \$$ \$$$$$$$${bcolors.ENDC}")
        print(("\t" * 14) + f"{bcolors.WARNING}WOW você é um cliente registrado, por conta disso os preços custam a metade do dobro!{bcolors.ENDC}")

        print(f'{bcolors.OKGREEN}Olá {user["name"]}, seja bem vindo!\n{bcolors.ENDC}')
        main.showusercategorys(self, user)




