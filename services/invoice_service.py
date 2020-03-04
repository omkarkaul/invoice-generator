from models.invoice_model import Invoice

def generate_invoice(data):
    invoice = Invoice(data)

    total = get_total(data)
    
    pages = calculate_number_of_pages(data)

    invoice.write_invoice_content(total, pages)

    invoice.output('invoice.pdf')

def get_total(data):
    total = 0.0

    products = data["products"]

    for product in products:
        quantity = products[product]["quantity"]
        price = products[product]["price"]

        value = quantity * price

        total += value
    
    return '%.2f'%total

def calculate_number_of_pages(data):
    products = data["products"]

    # return len(products) % 35

    ## for testing purposes
    return 2
