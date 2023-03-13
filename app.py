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


def is_registered(address):
    try:
        w = whois.whois(address)
    except Exception:
        return -1
    else:
        return bool(w.domain_name)


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
    result = is_registered(address)
    if result == -1:
        return template('result.tpl', output="Error: Domain is not registered")
    else:
        whois_info = whois.whois(address)
        if whois_info.domain_name:
            output = json.dumps(whois_info, indent=4, default=str)
        else: 
            output = "Error: Domain is invalid"
        return template('result.tpl', output=output)


if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)
