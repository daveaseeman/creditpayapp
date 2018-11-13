import os
from flask import Flask, request, redirect
from creditpay import get_payment_url

app = Flask(__name__)


@app.route("/")
def index():
    invoice_url = request.args.get('invoice_url')
    payment_url = None
    if invoice_url:
        payment_url = get_payment_url(invoice_url)
        print(payment_url)
    return redirect(payment_url)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
