#!/usr/bin/python3
""" Starts a Flask Web application """
from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ returns hello HBNB """
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns HBNB """
    return("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def txt(text):
    """ returns C with text variable value """
    text = text.replace('_', ' ')
    return('C %s' % (text))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyth(text="is cool"):
    """ returns Python with text variable value """
    text = text.replace('_', ' ')
    return('Python %s' % (text))


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """ displays only if n is an int """
    return('%d is a number' % (n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def temp(n=None):
    """ makes html template """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oore(n=None):
    """ number is even or odd """
    if n % 2 == 0:
        oore = 'even'
    else:
        oore = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, o_or_e=oore)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
