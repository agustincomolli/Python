from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)


# Database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://germancodoacodo:implementa1234@germancodoacodo.mysql.pythonanywhere-services.com/germancodoacodo$db-proyecto'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/db-proyecto'
#driver mysql://user:password@host:port/database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #para que no salga un warning

db = SQLAlchemy(app) #instancia de la base de datos
ma = Marshmallow(app) #instancia de la serializacion

#Modelo de la base de datos
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(70), unique=True)
    precio = db.Column(db.Float)
    stock = db.Column(db.Integer)
    imagen = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)
    def __init__(self, nombre, precio, stock, imagen, created_at, updated_at, deleted_at):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.imagen = imagen
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at


#Modelo de la base de datos
with app.app_context():
    db.create_all() #crea las tablas en la base de datos

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'precio', 'stock', 'imagen', 'created_at', 'updated_at', 'deleted_at')

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)


# Rutas

@app.route('/productos', methods=['GET'])
def get_productos():
    all_productos = Producto.query.all() #select * from productos
    result = productos_schema.dump(all_productos)
    return jsonify(result) #retorna todos los productos


@app.route('/producto/<id>', methods=['GET'])
def get_producto(id):
    producto = Producto.query.get(id)
    return producto_schema.jsonify(producto) #retorna el producto con el id especificado

@app.route('/producto', methods=['POST'])
def create_producto():
    print(request.json)
    nombre = request.json['nombre']
    precio = request.json['precio']
    stock = request.json['stock']
    imagen = request.json['imagen']
    fecha_actual = db.func.now()

    imagen_file = secure_filename(imagen.filename)
    imagen.save(imagen_file)

    new_producto = Producto(nombre, precio, stock, imagen, fecha_actual, None, None)
    db.session.add(new_producto)
    db.session.commit()
    return producto_schema.jsonify(new_producto) #retorna el producto creado

@app.route('/producto/<id>', methods=['PUT'])
def update_producto(id):
    producto = Producto.query.get(id) #select * from productos where id = id

    producto.nombre = request.json['nombre']
    producto.precio = request.json['precio']
    producto.stock = request.json['stock']
    producto.imagen = request.json['imagen']
    producto.updated_at = db.func.now()

    db.session.commit()
    return producto_schema.jsonify(producto) #retorna el producto actualizado


@app.route('/producto/<id>', methods=['DELETE'])
def delete_producto(id): #BORRADO LOGICO
    producto = Producto.query.get(id) #select * from productos where id = id
    producto.deleted_at = db.func.now()

    #db.session.delete(producto) #elimina el producto, si es un borrado permanente/fisico
    db.session.commit()
    return producto_schema.jsonify(producto) #retorna el producto eliminado



if __name__ == "__main__":
    app.run(debug=True, port=5000)