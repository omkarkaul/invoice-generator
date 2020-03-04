from fpdf import FPDF

class Invoice:
    def __init__(self, data):
        self.pdf = FPDF()
        
        self.data = data
        self.pdf.set_title(f'{self.data["company_name"]} invoice')
        self.pdf.set_title('invoice')
        self.pdf.set_font('Arial', 'B', 8)
    
    def write_invoice_content(self, total, pages):
        all_products = self.data['products']

        if len(all_products) <= 10:
            last_page = True
            # 10 or less products posted to service, thus only one page required
            self.pdf.add_page()

            self.write_header()
            self.write_content(total, all_products, last_page)
        else:
            # more than 10 products posted to service, 2 or more pages required
            for i in range(pages):
                if i == pages - 1: # if current page we're writing to is the last page, then set flag to true
                    last_page = True
                else:
                    last_page = False

                first_index = 0+i*10
                second_index = 10+i*10
 
                products = all_products[first_index: second_index] # products on a given page will be a sublist of all products...
                                                            # ...  based on page number so that a page always has 10 products
                self.pdf.add_page()

                self.write_header()
                self.write_content(total, products, last_page)

    def write_header(self):
        #image and title
        self.pdf.image('invoice_pic.png', 10, 8, 25, 25)
        self.pdf.set_font('Arial', size=22)
        self.write_text(34, 25, 'Generic Invoice Service')

        #invoice
        self.pdf.set_font('Arial', size=30)
        self.write_text(155, 30, 'Invoice')

        #date, invoice number, and period
        self.pdf.set_font('Arial', size=12)
        self.write_text(155, 38, f'Date: {self.data["date"]}')
        self.write_text(155, 44, f'Invoice Number: {self.data["invoice_number"]}')
        self.write_text(155, 50, f'Period: {self.data["period"]}')

        #to and from
        self.write_text(35, 54, f'From: {self.data["company_name"]}')
        self.write_text(35, 60, f'To: {self.data["invoice_to"]}')
    
    def write_content(self, total, products, last_page):
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
        y = 81

        for product in products:
            title = product['title']
            quantity = product['quantity']
            price = product['price']
            sku = product['sku']

            self.write_text(18, y, title)
            self.write_text(112, y, str(sku))
            self.write_text(142, y, str(quantity))
            self.write_text(172, y, str(price))
                    
            y += 5

        if last_page: #if the the page we're currently writing to is the last page, then..
            #draw total amount cell
            self.pdf.set_xy(140, 260)
            self.pdf.cell(55, 15, '', border=1)

            #draw total amount value
            self.pdf.set_font('Arial', 'B', 22)
            self.write_text(145, 270, '$' + str(total) + ' due')
    
    def write_notes(self):
        self.pdf.add_page()

        self.pdf.set_font('Arial', 'B', 14)
        self.write_text(10, 20, 'Notes:')
        self.pdf.set_line_width(0.5)
        self.pdf.line(10, 21, 25, 21)

        self.pdf.set_font('Arial', size=8)
        self.pdf.set_xy(10, 25)
        self.pdf.write(5, self.data['notes'])
        
    def write_text(self, x, y, text):
        self.pdf.text(x, y, text)

    def output(self, filename):
        self.pdf.output(filename, 'F')