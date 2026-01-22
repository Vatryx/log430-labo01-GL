"""
Product controller
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteur : Gabriel Lessard, 2026
"""
from daos.product_dao import ProductDAO

class ProductController:
    def __init__(self):
       self.dao = ProductDAO()

    def list_products(self):
        """ List all products """
        return self.dao.select_all()
        
    def create_product(self, product):
        """ Create a new product based on user inputs """
        self.dao.insert(product)

    def get_dao(self):
        return self.dao

    def shutdown(self):
        """ Close database connection """
        self.dao.close()
