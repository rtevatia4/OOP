from flask import (request, jsonify, Blueprint, url_for)
from .data_store import products

products_blueprint = Blueprint('products_api', __name__, url_prefix='/api/')

@products_blueprint.route('/products', methods=['GET'])
def list_products():
    return jsonify(products)

@products_blueprint.route('/products/<id>', methods=['GET'])
def get_product(id):
    response = None
    for product in products:
        if product['id'] == id:
            response = product
            break
    return jsonify(response)

@products_blueprint.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    data['id'] = str(len(products)+1)
    products.append(data)
    location = url_for('.get_product', id = data['id'], _external=True)
    response = jsonify(dict(product=data, location=location), 201)
    response.headers['Location'] = location
    return response

@products_blueprint.route('/products/<id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    update_product = None
    for product in products:
        if product['id'] == id:
            product.update(data)
            update_product = product
            break
    return jsonify(update_product)
