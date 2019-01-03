from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'Shri\'s Store',
        'items': [
            {
                'name': 'Item 1',
                'price': 15.99
            },
            {
                'name': 'Item 2',
                'price': 19.99
            }
        ]
    }
]

@app.route('/')
def home():
    return "Hello, world!"

# POST Add a Store {name: string}
@app.route("/store", methods=['POST'])
def add_store():
    data = request.get_json()
    for store in stores:
        if store['name'] == data['name']:
            return jsonify({
                'message': 'Store with this name already exists',
                'store': store
            })
    store = {
        'name': data['name'],
        'items': []
    }
    stores.append(store)
    return jsonify(store)

# GET Store named 'name'
@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'Store not found'})

# GET All stores
@app.route('/store')
def get_all_stores():
    return jsonify({'stores': stores})

# POST Add item to store {name: string, price: float}
@app.route('/store/<string:name>/item', methods=['POST'])
def add_item(name):
    data = request.get_json()
    for store in stores:
        if store['name'] == name:
            store['items'].append(data)
            return jsonify(data)
    return jsonify({'message': 'Store not found to add item'})

# GET All items in store
@app.route('/store/<string:name>')
def items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'Store not found'})

app.run(port=5000)