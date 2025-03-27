from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!/ olá mundo!'

@app.route('/<name>')
def hello_name(name):
    return f'Hello, {name}!'

@app.route('/soma/<num1>+<num2>')
def soma(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return f'Soma: {num1} + {num2} = {num1 + num2}'

@app.route('/sub/<num1>-<num2>')
def sub(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return f'sub: {num1} - {num2} = {num1 - num2}'

@app.route('/mul/<num1>*<num2>')
def mul(num1, num2):
    num1 = float(num1)
    num2 = int(num2)
    return f'mul: {num1} * {num2} = {num1 * num2}'

@app.route('/div/<num1>/<num2>')
def div(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    return f'div: {num1} / {num2} = {num1 / num2}'

@app.route('/veri/<num1>')
def veri(num1):
    try:
        num1 = float(num1)
        if num1 % 2 == 0:
            return 'par'
        else:
            return 'impar'
    except ValueError:
        return 'erro de valor'

if __name__ == '__main__':
    app.run(debug=True)
