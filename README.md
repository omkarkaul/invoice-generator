# Generic Invoice Generator

Dependencies:
- Pipenv (optional)
- Python 3.6
- Flask
- FPDF (PyFPDF, the python port of that old PHP library)
- awsebcli

(optional) To build and install dependencies, CD into your chosen project directory and type:
```
pipenv install
```
Then to run locally, run the following command:
```
python3 app.py
```

Aimed at creating invoices for basic stores with a simple product/price/quantity style format.

Post a collection of products as json object in some given format (written below), this service will then return an invoice with all the products an associated data in a PDF file.

At the moment, the only endpoint is a POST request on:
```
POST 0.0.0.0:8080/api/invoice
```
Which requires the header `Content-Type: application/json`
JSON format for request:
```
{
	"company_name": "test-company-name",
	"products": {
		"1": {
			"title": "test-product-one",
			"price": 12.99,
			"quantity": 4,
			"sku":1
		}, ... (add more products here)
	},
	"invoice_number":1,
	"notes": "test note",
	"date": "02/03/20",
	"invoice_to": "test-buyer",
	"period": "28 days"
}
```


## TODO:

- [ ] Add pagination support (at the moment a maximum of 35 products are supported, producing one page)
- [ ] Deploy on AWS with Beanstalk & EC2