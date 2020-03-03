from models.invoice_model import Invoice

def generate_invoice(data):
    invoice = Invoice(data)

    total = get_total(data)

    invoice.write_invoice_content(total)

    invoice.output('invoice.pdf')

def get_total(data):
    total = 0

    products = data["products"]

    for product in products:
        quantity = products[product]["quantity"]
        price = products[product]["price"]

        value = quantity * price

        total += value
    
    return total