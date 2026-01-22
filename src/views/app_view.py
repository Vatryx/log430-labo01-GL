from views.user_view import UserView
from views.product_view import ProductView
from controllers.product_controller import ProductController
from controllers.user_controller import UserController

class AppView:

    def __init__(self):
        self.user_controller = UserController()
        self.product_controller = ProductController()
    def execute_app(self):
        while True:
            print("\n===== LE MAGASIN DU COIN =====")
            print("1. Montrer la liste d'utilisateurs")
            print("2. Ajouter un utilisateur")
            print("3. Montrer la liste d'items")
            print("4. Ajouter un item")
            print("5. Quitter l'appli")

            choice = input("Choisir une option: ").strip()

            if choice in ('1', '2'):
                UserView.show_options(choice,self.user_controller)
            elif choice in ('3', '4'):
                ProductView.show_options(choice, self.product_controller)
            elif choice == '5':
                self.user_controller.shutdown()
                self.product_controller.shutdown()
                break
            else:
                print("Cette option n'existe pas.")
