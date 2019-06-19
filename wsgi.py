# wsgi.py
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

PRODUCTS = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'fatal' }
]

@app.route('/')
def check():
    return "Hello World!"

@app.route('/api/v1/products', methods=['GET', 'POST'])
def read_all():
    if request.method == 'GET':
        return jsonify(PRODUCTS)
    elif request.method == 'POST':
        post_request = request.get_json()
        print(post_request)
        if 'name' not in post_request:
            abort(400)
        new_element = {'id': (len(PRODUCTS) + 1),'name': post_request['name']}
        PRODUCTS.append(new_element)
        return "", 201

@app.route('/api/v1/products/<int:post_id>', methods=['GET', 'DELETE'])
def read_id(post_id):
    if request.method == 'GET':
        for product in PRODUCTS:
            print(product)
            if product['id'] == post_id:
                return jsonify(product)
    elif request.method == 'DELETE':
        for product in PRODUCTS:
            if product['id'] == post_id:
                PRODUCTS.remove(product)
                return "", 204
