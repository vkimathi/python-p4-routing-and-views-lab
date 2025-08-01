#!/usr/bin/env python3

from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    """Display numbers from 0 to parameter-1 on separate lines"""
    if parameter <= 0:
        return "Parameter must be positive", 400
    numbers = '\n'.join(str(i) for i in range(parameter))
    return Response(numbers, mimetype='text/plain')

@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math_operations(num1, operation, num2):
    """Perform basic math operations on two numbers"""
    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == 'div':
            if num2 == 0:
                return "Error: Division by zero", 400
            result = num1 / num2
        elif operation == '%':
            result = num1 % num2
        else:
            return "Error: Invalid operation. Use +, -, *, div, or %", 400
        
        return f"Result: {result}", 200
    except Exception as e:
        return f"Error: {str(e)}", 400

if __name__ == '__main__':
    app.run(port=5555, debug=True)