# Receipt Generator
from pyscript import document, display


def create_order(e):
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")


    subtotal = float(prod1.value) * prod1.checked + float(prod2.value) * prod2.checked + float(prod3.value) * prod3.checked + float(prod4.value) * prod4.checked + float(prod5.value) * prod5.checked


    vat= subtotal * 0.12
    total = subtotal + vat


    display("Subtotal: ₱" + str(subtotal), target="show")
    display("Vat: ₱" + str(vat), target="show")
    display("Total: ₱" + str(total), target="show")