from flask import Flask, request, flash, render_template
from flask_restful import Api, Resource, reqparse
from addition import Addition
from subtraction import Subtraction
from multiplication import Multiplication
from division import Division
app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
api = Api(app)


api.add_resource(Addition, '/add/<int:num1>/<int:num2>')
api.add_resource(Subtraction, '/subtract/<int:num1>/<int:num2>')
api.add_resource(Multiplication, '/multiply/<int:num1>/<int:num2>')
api.add_resource(Division, '/divide/<int:num1>/<int:num2>')


if __name__ == '__main__':
    app.run(debug=True,
        port=5050,
        host="0.0.0.0")
