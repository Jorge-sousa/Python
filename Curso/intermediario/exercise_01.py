def catalog():
    cell = {
        'iphone 13': 3800,
        'samsung s22': 4000,
        'xiaomi note 10': 1350
    }

    notebook = {
        'dell': 3300,
        'samsung': 2700,
        'lenovo': 2100,
        'acer': 1850 
    }

    products = ['cell', 'notebook']
    products_brands_cell = tuple(cell.items())
    products_brands_note = tuple(notebook.items())

    product_on_sale = input('Informe o produto que está em promoção: ').lower().strip()

    if product_on_sale in products:
        brand = input('Informe a marcar: ').lower().strip()
        if brand in products_brands_cell or products_brands_note:
            return brand

    else:
        return 'Error, product not found'


# def discount(product):
#     def product_promotion(products):


print(catalog())