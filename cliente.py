import sqlalchemy
from flask import  request, jsonify
from start import *
from sqlalchemy.exc import  *
from flask_cors import CORS,cross_origin

class cliente(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True)
    nombre_cliente = db.Column(db.String(45))
    apellido_cliente = db.Column(db.String(45))
    pasaporte_cliente = db.Column(db.String(45))
    licencia_cliente = db.Column(db.String(45))
    correo_cliente = db.Column(db.String(45))
    telefono_cliente1= db.Column(db.String(45))
    telefono_cliente2= db.Column(db.String(45))

    def __init__(self,nombre_cliente,apellido_cliente,pasaporte_cliente,licencia_cliente,correo_cliente,telefono_cliente1,telefono_cliente2):
        self.nombre_cliente=nombre_cliente
        self.apellido_cliente=apellido_cliente
        self.pasaporte_cliente=pasaporte_cliente
        self.licencia_cliente=licencia_cliente
        self.correo_cliente=correo_cliente
        self.telefono_cliente1=telefono_cliente1
        self.telefono_cliente2 = telefono_cliente2

    db.create_all()

    class clienteSchema(ma.Schema):

        class Meta:
            fields=('id_cliente','nombre_cliente','apellido_cliente','pasaporte_cliente','licencia_cliente','correo_cliente','telefono_cliente1','telefono_cliente2')

    cliente_schema= clienteSchema()
    clientes_schema=clienteSchema(many=True)

    @app.route('/', methods=['GET'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def raiz():

        return 'hola funciono'

    @app.route('/getClientes', methods=['GET'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def cliente_data():
        data = cliente.query.all()
        result = cliente.clientes_schema.dump(data)
        return jsonify(result)

    @app.route('/getClienteBy/<id>', methods=['GET'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def get_ClienteBy(id):
        data = cliente.query.get(id)
        if data == None:
            return "Not mach found"
        return cliente.cliente_schema.jsonify(data)

    @app.route('/addClient', methods=['POST'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def addcliente():

        # id = request.json['id']
        nombre_cliente = request.json['nombre_cliente']
        apellido_cliente = request.json['apellido_cliente']
        pasaporte_cliente = request.json['pasaporte_cliente']
        licencia_cliente = request.json['licencia_cliente']
        correo_cliente = request.json['correo_cliente']
        telefono_cliente1 = request.json['telefono_cliente1']
        telefono_cliente2 = request.json['telefono_cliente2']

        newcliente = cliente(nombre_cliente, apellido_cliente, pasaporte_cliente, licencia_cliente, correo_cliente,telefono_cliente1,telefono_cliente2)

        db.session.add(newcliente)
        db.session.commit()
        return "OK"

    @app.route('/updateCliente/<id>', methods=['PUT'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def updateCliente(id):
        data = cliente.query.get(id)
        print(data)
        # id = request.json['id']

        nombre_cliente = request.json['nombre_cliente']
        apellido_cliente = request.json['apellido_cliente']
        pasaporte_cliente = request.json['pasaporte_cliente']
        licencia_cliente = request.json['licencia_cliente']
        correo_cliente = request.json['correo_cliente']
        telefono_cliente1 = request.json['telefono_cliente1']
        telefono_cliente2 = request.json['telefono_cliente2']

        # data.id = id

        data.nombre_cliente = nombre_cliente
        data.apellido_cliente = apellido_cliente
        data.pasaporte_cliente = pasaporte_cliente
        data.licencia_cliente = licencia_cliente
        data.correo_cliente = correo_cliente
        data.telefono_cliente1 = telefono_cliente1
        data.telefono_cliente2 = telefono_cliente2



        db.session.commit()
        return "OK"

    @app.route('/delCliente/<id>', methods=['DELETE'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def delete_cliente(id):
        data = cliente.query.get(id)
        db.session.delete(data)
        db.session.commit()
        return cliente.cliente_schema.jsonify(data)




