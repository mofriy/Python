import flask
from flask import Flask, request

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

@app.route("/")
def root():
    return flask.render_template(
        'index.html'
    )

@app.route('/primal', methods=['GET'])
def primal():
    num = request.args.get('number')

    if num == None:
        num = 1
        res = 'Ни то, ни сё'
    else:
        num = int(num)

    def primal(a):
        if a <= 1:
            return -1
        if a%2 == 0:
            return 0
        i = 3
        while i <= round(a**0.5):
            if a%i == 0:
                return 0
            i += 2
        return 1
    f = primal(num)
    if f == -1:
        res = 'Ни то, ни сё'
    elif f == 1:
        res = 'Primal'
    else:
        res = "Primaln't"

    return flask.render_template(
        'primal.html',
        res=res,
        num=num,
        method=request.method
    )

@app.route('/gcd', methods=['GET'])
def gcd():
    num1 = request.args.get('number1')
    num2 = request.args.get('number2')

    if num1 == None:
        num1 = 0
    else:
        num1 = int(num1)
    if num2 == None:
        num2 = 0
    else:
        num2 = int(num2)

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a%b)

    res = gcd(num1,num2)

    return flask.render_template(
        'gcd.html',
        res=res,
        num1=num1,
        num2=num2,
        method=request.method
    )

@app.route("/egcd", methods = ['GET'])
def egcd():
    num1 = request.args.get('number1')
    num2 = request.args.get('number2')

    if num1 == None:
        num1 = 0
    else:
        num1 = int(num1)    
    if num2 == None:
        num2 = 0
    else:
        num2 = int(num2)
    def egcd (a, b):
        if b == 0:
            return (1, 0, a)
        else:
            (x, y, d) = egcd(b, a % b)
        return (y, x - (a // b) * y, d)
    
    a, b, c = egcd(num1, num2)
    res = str(a) + "*" + str(num1) + " + " + str(b) + "*" + str(num2) + " = " + str(c)

    return flask.render_template(
        'egcd.html',
        res=res,
        num1=num1,
        num2=num2,
        method=request.method
    )


@app.route("/system", methods = ['GET'])
def system():
    num = request.args.get('number')
    sys = request.args.get('system')

    if num == None:
        num = 0
    else:
        num = int(num)
    if sys == None:
        sys = 10
    else:
        sys = int(sys)
    res = '0'
    def a(value,base):
        newint = ''
        while value > 0:
            x = value % base
            if x < 10:
                newint = str(x) + newint
            else:
                newint = chr(x + ord('A') - 10) + newint
            value = value // base
        return newint

    res = a(num, sys)
    return flask.render_template(
        'system.html',
        res=res,
        num=num,
        sys=sys,
        method=request.method
    )


if __name__ == '__main__':
    app.run(debug=True)
