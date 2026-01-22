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

