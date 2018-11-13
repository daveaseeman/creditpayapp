import requests
from bs4 import BeautifulSoup

def get_payment_url(invoice_url):
    invoice_content = requests.get(invoice_url).content
    parsed_content = BeautifulSoup(invoice_content)
    invoice_amount = float(parsed_content.find("td", id="total-amount").contents[0].replace("$", "").replace(",", ""))
    credit_amount = str(round(invoice_amount/0.97, 2))
    payment_url = 'https://www.paypal.me/fractalhardware/' + credit_amount
    return payment_url
