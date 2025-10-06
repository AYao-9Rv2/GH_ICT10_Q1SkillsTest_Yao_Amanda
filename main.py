from pyscript import display, document

def place_order(e):
    # get customer info
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    contnum = document.getElementById("contnum").value

    # prices
    earrings_price = 50
    necklace_price = 80
    rings_price = 42
    tax_rate = 0.08

    price = 0

    # needed help with this, sorry sir :<
    if document.getElementById("earrings").checked:
        price = price + earrings_price
    if document.getElementById("necklace").checked:
        price = price + necklace_price
    if document.getElementById("rings").checked:
        price = price + rings_price

    total = price + (price * tax_rate)

    document.getElementById("div1").innerHTML = ""

    display(f"Order for: {name}", target="div1")
    display(f"Contact number: {contnum}", target="div1")
    display(f"Delivery address: {address}", target="div1")
    display(f"Total: ₱{total:.2f}", target="div1")
