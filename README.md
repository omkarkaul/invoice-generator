# Generic Invoice Generator

Dependencies:
- Python 3.6
- Flask
- FPDF (PyFPDF, the python port of that old PHP library)
- awsebcli

Aimed at creating invoices for basic stores with a simple product/price/quantity style format.

Post a collection of products as json object in some given format (TBD), this service will then return an invoice with all the products an associated data in a PDF file.