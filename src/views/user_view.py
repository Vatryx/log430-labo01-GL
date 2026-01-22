"""
User view
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from models.user import User
from controllers.user_controller import UserController

class UserView:
    @staticmethod
    def show_options(choice, controller_user):
        """ Show menu with operation options which can be selected by the user """
        if choice == '1':
            users = controller_user.list_users()
            UserView.show_users(users)
        elif choice == '2':
            name, email = UserView.get_inputs_user()
            user = User(None, name, email)
            controller_user.create_user(user)
    @staticmethod
    def show_users(users):
        """ List users """
        print("\n".join(f"{user.id}: {user.name} ({user.email})" for user in users))


    @staticmethod
    def get_inputs_user():
        """ Prompt user for inputs necessary to add a new user """
        name = input("Nom d'utilisateur : ").strip()
        email = input("Adresse courriel : ").strip()
        return name, email