from models.invoice_model import Invoice


def generate_invoice(data):
    """ This function performs necessary logic for generating an invoice """
    invoice = Invoice(data)

    total = get_total(data)

    pages = calculate_number_of_pages(data)

    invoice.write_invoice_content(total, pages)

    invoice.write_notes()

    invoice.output('invoice.pdf')


def get_total(data):
    """ This function calculates a total amount due, for the passed data, to be written to the invoice """
    total = 0.0

    products = data["products"]

    for product in products:
        print(product)
        quantity = product["quantity"]
        price = product["price"]

        value = quantity * price

        total += value

    return '%.2f' % total


def calculate_number_of_pages(data):
    """ Uses the number of products to calculate the number of pages required in the invoice """
    products = data["products"]

    return int(len(products) / 10) + 1
