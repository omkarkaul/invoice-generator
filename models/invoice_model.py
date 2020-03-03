from fpdf import FPDF

class Invoice:
    def __init__(self, data):
        self.pdf = FPDF()
        
        self.data = data
        self.pdf.set_title(f'{self.data["company_name"]} invoice')
        self.pdf.set_title('invoice')
        self.pdf.set_font('Arial', 'B', 8)
    
    def write_invoice_content(self, total):
        self.pdf.add_page()

        self.write_header()
        self.write_content(total)

    def write_header(self):
        #image and title
        self.pdf.image('invoice_pic.png', 10, 8, 25, 25)
        self.pdf.set_font('Arial', size=22)
        self.write_text(34, 25, 'Generic Invoice Service')

        #invoice
        self.pdf.set_font('Arial', size=30)
        self.write_text(155, 30, 'Invoice')

        #date and invoice number
        self.pdf.set_font('Arial', size=12)
        self.write_text(155, 38, f'Date: {self.data["date"]}')
        self.write_text(155, 44, f'Invoice Number: {self.data["invoice_number"]}')

        #to and from
        self.write_text(35, 54, f'From: {self.data["company_name"]}')
        self.write_text(35, 60, f'To: {self.data["invoice_to"]}')
    
    def write_content(self, total):
        #draw cells
        self.pdf.set_line_width(0.2)
        self.pdf.set_xy(15, 70)
        self.pdf.cell(180, 190, '', border=1)
        self.pdf.set_xy(15, 70)
        self.pdf.cell(125, 190, '', border=1)
        self.pdf.set_xy(110, 70)
        self.pdf.cell(30, 190, '', border=1)
        self.pdf.set_xy(140, 70)
        self.pdf.cell(30, 190, '', border=1)
        self.pdf.set_xy(140, 260)
        self.pdf.cell(55, 15, '', border=1)
        
        #write titles and underline (line width 0.5mm, then reset to default)
        self.pdf.set_font('Arial', 'B', 12)
        self.write_text(18, 75, 'Product name:')
        self.write_text(112, 75, 'SKU:')
        self.write_text(142, 75, 'Quantity:')
        self.write_text(172, 75, 'Price:')
        self.pdf.set_line_width(0.3)
        self.pdf.line(15, 76.5, 195, 76.5)
        self.pdf.set_line_width(0.2)

        self.pdf.set_font('Arial', size=10)
        products = self.data["products"]
        y = 81

        for _ in range(7):
            for product in products:
                title = products[product]["title"]
                quantity = products[product]["quantity"]
                price = products[product]["price"]
                sku = products[product]["sku"]

                self.write_text(18, y, title)
                self.write_text(112, y, str(sku))
                self.write_text(142, y, str(quantity))
                self.write_text(172, y, str(price))
                        
                y += 5

        self.pdf.set_font('Arial', 'B', 22)
        self.write_text(145, 270, '$' + str(total) + ' due')
        
    def write_text(self, x, y, text):
        self.pdf.text(x, y, text)

    def output(self, filename):
        self.pdf.output(filename, 'F')