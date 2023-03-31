from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Division(Resource):
    def get(self, num1, num2):
        if num2 == 0:
            return {'error': 'Cannot divide by zero'}
        return {'result': num1 / num2}

api.add_resource(Division, '/divide/<int:num1>/<int:num2>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
