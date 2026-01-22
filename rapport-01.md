## Gabriel Lessard - 20 janvier 2026
### Lab 01 - LOG430

### Question 1 
Quelles commandes avez-vous utilisées pour effectuer les opérations UPDATE et DELETE dans MySQL ? Avez-vous uniquement utilisé Python ou également du SQL ? Veuillez inclure le code pour illustrer votre réponse.

La commande << execute >> du curseur nous permet d'effectuer des commandes SQL sur les tables dans la base de donnée.
De plus, la commande commit nous permet de confirmer les modifications que nous avons fait à la table en question.
``` py
def update(self, user):
    """ Update given user in MySQL """
    self.cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (user.name, user.email, user.id))
    self.conn.commit()
    return self.cursor.rowcount

def delete(self, user_id):
    """ Delete user from MySQL with given user ID """
    self.cursor.execute("DELETE FROM users WHERE id=%s", (user_id))
    self.cursor.commit()
    return self.cursor.rowcount
``` 

### Question 2 
Quelles commandes avez-vous utilisées pour effectuer les opérations dans MongoDB ? Avez-vous uniquement utilisé Python ou également du SQL ? Veuillez inclure le code pour illustrer votre réponse.

MongoDB est un style de base de donnée qui utilise le format JSON (clé, valeur). La syntaxe est donc forcément différente et unique pour pouvoir effectuer des opérations dans la base de donnée. Les tables sont appelées des collections et pour effectuer les opérations SELECT INSERT UPDATE DELETE il faut utiliser les commandes find, insert_one, update_one et delete_one de la collection voulue.
``` py
def select_all(self):
        """ Select all users from MongoDB """
        users = []
        for doc in self.collection.find():
            users.append(
                User(
                    str(doc["_id"]),
                    doc.get("name"),
                    doc.get("email")
                )
            )
        return users

    def insert(self, user):
        """ Insert given user into MongoDB """
        new_user = self.collection.insert_one({
            "name": user.name,
            "email": user.email
        })
        return str(new_user.inserted_id)


    def update(self, user):
        """ Update given user in MongoDB """
        update_user = self.collection.update_one(
            { "_id": ObjectId(user.id) },
            {
                "$set": {
                    "name": user.name,
                    "email": user.email
                }
            }
        )
        return update_user.matched_count == 1


    def delete(self, user_id):
        """ Delete user from MongoDB with given user ID """
        delete_filter = { "_id": ObjectId(user_id) }
        delete_user = self.collection.delete_one(delete_filter)
        return delete_user.deleted_count == 1
```
### Question 3 
Comment avez-vous implémenté votre product_view.py ? Est-ce qu’il importe directement la ProductDAO ? Veuillez inclure le code pour illustrer votre réponse.


Dans ce laboratoire, nous avons 2 vues, une pour les << users >> et une pour les << products >>. Chacun ont leur propre méthodes pour pouvoir effectuer des actions dans l'application. Cependant, j'ai regroupé les 2 vues dans un fichier que j'ai nommé << app_view.py >> qui s'occupe de faire l'affichage et qui détermine le temps que l'application s'exécute qui dépend des choix de l'utilisateur. Important, les vues n'ont aucune affaire à accéder au DAO puisque techniquement ils n'ont pas conscience de leur existance. Seulement les contrôleurs des deux modèles devrait agir comme pont pour effectuer les opérations nécessaires. Voici ci-dessous dans l'ordre mon product_view.py et app_view.py
```py
"""
Product view
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel Lessard, 2026
"""

from models.product import Product

class ProductView:
    @staticmethod
    def show_options(choice, controller_product):
          """ Show menu with operation options which can be selected by the user """
         
          if choice == '3':
            products = controller_product.list_products()
            ProductView.show_products(products)
          elif choice == '4':
            name, brand, price = ProductView.get_inputs_product()
            product = Product(None,name, brand, price)
            controller_product.create_product(product)
          else:
            print("Cette option n'existe pas.")
            
    
    @staticmethod
    def show_products(products):
        """ List products """
        print("\n".join(f"{product.id}: {product.name} {product.brand} {product.price}" for product in products))

    @staticmethod
    def get_inputs_product():
        """ Prompt user for inputs necessary to add a new product """
        name = input("Nom de l'item : ").strip()
        brand = input("Marque de l'item: ").strip()
        price = input("Prix de l'item: ").strip()
        return name, brand, price
```

```py
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

```
###  Question 4 
Si nous devions créer une application permettant d’associer des achats d'articles aux utilisateurs (Users → Products), comment structurerions-nous les données dans MySQL par rapport à MongoDB ?

Dans MySQL, pour créer une association,  il faudrait garder un attribut/propriété qui fait le lien entre les deux tables pour savoir quel produit a été acheté par quel utilisateur. En faisant cela, il va être facile de retracer le lien entre le produit et l'utilisateur en question. Dans le cas de MongoDB, c'est un peu le même principe, en utilisant ce qui s'appelle la méthode des références manuelles, nous stockerons l'id du user dans la collection product pour créer cette association entre les deux. 