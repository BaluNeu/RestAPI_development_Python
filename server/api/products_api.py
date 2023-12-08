from flask import (request, jsonify, Blueprint)
from .data_store import products

products_blueprint = Blueprint('products_api', __name__, url_prefix='/api/')

@products_blueprint.route('/products',methods = ['GET'])
def list_products():
    return jsonify(products)

@products_blueprint.route('/products/product_id', methods=['GET'])
def get_product(product_id):
    result = next((product for product in products if product['id'] == product_id), None)
    return jsonify(result)

@products_blueprint.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    data['id'] = str(len(products) + 1)
    products.append(data)
    location = url_for('.get_product', product_id = data['id'], _external=True)
    response = jsonify(dict(product=data, location=location))
    response.headers['Location'] = location
    return response, 201


@products_blueprint.route('/products/product_id', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    updated_product = None
    for product in products:
        if product['id'] == product_id:
            product.update(data )
            updated_product = product
    return jsonify(updated_product)