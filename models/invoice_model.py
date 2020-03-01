from fpdf import FPDF

class Invoice:
    def __init__(self, data):
        self.pdf = FPDF()
        
        self.data = data
        # self.pdf.set_title(f'{data.title} invoice')
        self.pdf.set_title('invoice')
        self.pdf.set_font('Arial', 'B', 8)
    
    def write_invoice_content(self):
        self.pdf.add_page()

        self.pdf.text(20, 30, 'test :D')

    def output(self, filename):
        self.pdf.output(filename, 'F')