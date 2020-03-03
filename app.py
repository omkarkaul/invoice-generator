from flask import Flask, request, make_response, send_file
from services import invoice_service

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    return "Invoice generator!"

@app.route("/api/invoice", methods = ["POST"])
def generate_invoice():
    if request.is_json:
        data = request.get_json()

        invoice_service.generate_invoice(data)

        return send_file('./invoice.pdf', attachment_filename='invoice.pdf')
    
    return make_response(('Please include correct "content-type" header!', 400))

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=8080, debug=True)