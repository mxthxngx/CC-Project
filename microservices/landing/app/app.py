from flask import Flask, request, flash, render_template
import sys
from flask_restful import Api, Resource, reqparse
from addition.app import Addition
from subtraction.app import Subtraction
from multiplication.app import Multiplication
from division.app import Division
app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
api = Api(app)


api.add_resource(Addition, '/add/<int:num1>/<int:num2>')
api.add_resource(Subtraction, '/subtract/<int:num1>/<int:num2>')
api.add_resource(Multiplication, '/multiply/<int:num1>/<int:num2>')
api.add_resource(Division, '/divide/<int:num1>/<int:num2>')



@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = request.form.get("first")
    number_2 = request.form.get('second')
    operation = request.form.get('operation')
    result = 0
    if operation == 'add':
        add = Addition()
        result = add.get(int(number_1), int(number_2))
    elif operation == 'minus':
        sub = Subtraction()
        result = sub.get(int(number_1), int(number_2))
    elif operation == 'multiply':
        mult = Multiplication()
        result = mult.get(int(number_1), int(number_2))
    elif operation == 'divide':
        div = Division()
        result = div.get(int(number_1), int(number_2))

    flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )