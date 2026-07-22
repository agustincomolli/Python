from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from PIL import Image
from flask_cors import CORS  # Importa el módulo CORS

app = Flask(__name__, static_folder='static')
CORS(app)  # Aplica CORS a tu aplicación Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/db-proyecto'
db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(200))

    def __init__(self, name, price, stock, image):
        self.name = name
        self.price = price
        self.stock = stock
        self.image = image

# Ruta para obtener la lista de productos
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = []

    for product in products:
        product_data = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'stock': product.stock,
            'image': product.image
        }
        product_list.append(product_data)

    return jsonify(product_list)

@app.route('/products', methods=['POST'])
def create_product():
    name = request.form.get('name')
    price = request.form.get('price')
    stock = request.form.get('stock')
    image = request.files.get('image')

    # Guardar la imagen en el servidor
    image_filename = secure_filename(image.filename)
    image.save(image_filename)

    # Crear el producto
    product = Product(name, price, stock, image_filename)
    db.session.add(product)
    db.session.commit()

    return jsonify({'message': 'Producto creado exitosamente'}), 201


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()