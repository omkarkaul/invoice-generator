from models.pdf_model import Invoice

def generate_invoice(data):
    invoice = Invoice(data)

    invoice.write_invoice_content()

    invoice.output('invoice.pdf')