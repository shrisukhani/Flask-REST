from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authorize, identity

app = Flask(__name__)
app.secret_key = "shri"
api = Api(app)
jwt = JWT(app, authenticate, identity)

items = []


class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return item if item else {'message': 'Item not found'}, 404

    def post(self, name):
        item = {'name': name, 'price': 12.99}
        items.append(item)
        return item, 201


api.add_resource(Item, '/item/<string:name>')

app.run(port=5000)
