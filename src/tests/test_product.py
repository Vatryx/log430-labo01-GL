from daos.product_dao import ProductDAO
from models.product import Product

dao = ProductDAO()

def test_product_select():
     product_list = dao.select_all()
     assert len(product_list) >= 3

def test_product_insert():
    product = Product(None, 'nom Test', 'Marque Test',99.99)
    dao.insert(product)
    product_list = dao.select_all()
    names = [p.name for p in product_list]
    assert product.name in names

def test_product_update():
    product = Product(None, 'nom Test', 'Marque Test',99.99)
    assigned_id = dao.insert(product)

    corrected_name = 'Mon Nom'
    product.id = assigned_id
    product.name = corrected_name
    dao.update(product)

    product_list = dao.select_all()
    names = [p.name for p in product_list]
    assert corrected_name in names

    # cleanup
    dao.delete(assigned_id)

def test_product_delete():
    product = Product(None, 'nom Testtttt','Marque Test', 99.99)
    assigned_id = dao.insert(product)
    dao.delete(assigned_id)

    new_dao = ProductDAO()
    product_list = new_dao.select_all()
    names = [p.name for p in product_list]
    assert product.name  not in names