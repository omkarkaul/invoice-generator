from models.invoice_model import Invoice

def generate_invoice(data):
    invoice = Invoice(data)

    total = get_total(data)
    
    pages = calculate_number_of_pages(data)

    invoice.write_invoice_content(total, pages)

    invoice.write_notes()

    invoice.output('invoice.pdf')

def get_total(data):
    total = 0.0

    products = data["products"]

    for product in products:
        quantity = product["quantity"]
        price = product["price"]

        value = quantity * price

        total += value
    
    return '%.2f'%total

def calculate_number_of_pages(data):
    products = data["products"]

    return int(len(products) / 10) + 1
