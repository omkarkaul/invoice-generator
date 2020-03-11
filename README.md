# Generic Invoice Generator

Aimed at creating invoices for basic stores with a simple product/price/quantity style format.

Post a collection of products as a json object in some given format (written below), this service will then return an invoice with all the products and associated data in a PDF file.

For now, I've added basic pagination support so that a page can only have 10 products on it (e.g. 12 products will produce an invoice with 2 pages, 10 products on the first page and 2 products on the second). This logic also means that the "total amount due" is only written on the last page!

## Prerequisites

Dependencies:
- Pipenv (optional)
- Python 3.6
- Flask
- FPDF (PyFPDF, the python port of that old PHP library)
- awsebcli

## Getting started

(optional) To build and install dependencies, CD into your chosen project directory and type:
```
pipenv install
```
Then to run locally, run the following command:
```
python3 app.py
```

## Using the service

At the moment, the only endpoint is a POST request on:
```
POST 0.0.0.0:8080/api/invoice
```
Which requires the header `Content-Type: application/json`

JSON format for request:
```
{
	"company_name": "test-company-name",
	"products": [
		{
			"title": "test-product-one",
			"price": 12.99,
			"quantity": 4,
			"sku":1
		}, ... (add more products here)
	],
	"invoice_number":1,
	"notes": "test note",
	"date": "02/03/20",
	"invoice_to": "test-buyer",
	"period": "28 days"
}
```

## TODO:

- [x] Add pagination support (at the moment a maximum of 10 products are supported per page)
- [ ] Handle edge cases (e.g. product name is too long)
- [ ] Deploy on AWS with Beanstalk & EC2
- [ ] Add error handling for missing keys in posted JSON object
- [ ] Add misc error handling