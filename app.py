# Toy Interview Question (solution by Christopher Hampson)
#
# Requires:
# Bottle https://bottlepy.org/docs/dev/
# python-whois https://pypi.org/project/python-whois/
#
# h3 font: Montserrat (regular 400) from Google Fonts


import whois
import json
from bottle import response, route, request, Bottle, run, template, SimpleTemplate, get, post


@route('/')
def index():
    return template('index.tpl')


app = Bottle()


@app.get('/')
def entry_form():
    return template('index.tpl')


@app.post('/result')
def submit_form():
    address = request.forms.get('address')
    whois_info = whois.whois(address)
    pretty_whois = json.dumps(whois_info, indent=4, default=str)
    return template('result.tpl', pretty_whois=pretty_whois)


if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)
