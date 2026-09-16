#SKU + Receipt Generator


from pyscript import document, display


def generate_sku(e):
    category = document.getElementById("category").value
    product = document.getElementById("product").value
    stock = document.getElementById("stock").value

    product = product.upper()

    sku = category + product[:3] + stock

    display("SKU: " + sku, target="show")