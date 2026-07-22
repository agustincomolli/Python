from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # PERMITE QUE SE PUEDA CONSUMIR LA API DESDE CUALQUIER DOMINIO

# TENEMOS EL OBJETO PRODUCTO

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price
        }

products = [
    Product(1, 'asdasd', 2132),
    Product(2, 'Mouse', 40),
    Product(3, 'Keyboard', 60),
    Product(4, 'Monitor', 200)
]
# ARRACAMOS LA APLICACION FLASK Y LA PRIMER RUTA GET

@app.route('/all', methods=['GET'])
def get_all():
    return jsonify([product.to_json() for product in products])

@app.route('/all/<int:id>', methods=['GET'])
def get_product_by_id(id):
    for product in products:
        if product.id == id:
            return jsonify(product.to_json())
        
    return jsonify({'message': 'Product not found'})

@app.route('/create', methods=['POST']) 
def create_product():
    data = request.get_json() # OBTENEMOS DEL BODY EL JSON
    for item in data:
        name = item['name']
        price = item['price']
        id = len(products) + 1
        new_product = Product(id, name, price) # CREAMOS EL NUEVO PRODUCTO
        products.append(new_product) # AGREGAMOS EL NUEVO PRODUCTO A LA LISTA

    return jsonify(new_product.to_json())
    

@app.route('/update/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json() # OBTENEMOS DEL BODY EL JSON
    for item in data:
        name = item['name']
        price = item['price']
        for product in products:
            if product.id == id:
                product.name = name
                product.price = price
            return jsonify(product.to_json())
    

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_product(id):
    for product in products:
        if product.id == id:
           products.remove(product)
           return jsonify(products)

    return jsonify({'message': 'Product not found'})

if __name__ == '__main__':
    app.run(debug=True, port=4000)
