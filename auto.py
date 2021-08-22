import sqlalchemy
from flask import request, jsonify
from start import *
from sqlalchemy.exc import *
from flask_cors import CORS, cross_origin


class auto(db.Model):
    id_auto = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(45))
    modelo = db.Column(db.String(45))
    categoria = db.Column(db.String(45))
    puertas = db.Column(db.Integer)
    precio = db.Column(db.Integer)
    id_socio = db.Column(db.Integer)

    def __init__(self, marca, modelo, categoria, puertas, precio, id_socio):

        #self.id_auto = id_auto
        self.marca = marca
        self.modelo = modelo
        self.categoria = categoria
        self.puertas = puertas
        self.precio = precio
        self.id_socio = id_socio

    db.create_all()

    class autoSchema(ma.Schema):
        class Meta:
            fields = ('id_auto', 'marca', 'modelo', 'categoria', 'puertas', 'precio','id_socio')

    auto_schema = autoSchema()
    autos_schema = autoSchema(many=True)

    @app.route('/getAutos', methods=['GET'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def auto_data():
        data = auto.query.all()
        result = auto.autos_schema.dump(data)
        return jsonify(result)

    @app.route('/getAutoBy/<id>', methods=['GET'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def get_autoBy(id):
        data = auto.query.get(id)
        if data == None:
            return "Not mach found"
        return auto.auto_schema.jsonify(data)

    @app.route('/addAuto', methods=['POST'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def addauto():
     #   id_auto = request.json['id_auto']
        marca = request.json['marca']
        modelo = request.json['modelo']
        categoria = request.json['categoria']
        puertas = request.json['puertas']
        precio = request.json['precio']
        id_socio = request.json['id_socio']

        newauto = auto(marca, modelo, categoria, puertas, precio, id_socio)

        db.session.add(newauto)
        db.session.commit()
        return "OK"

    @app.route('/updateAuto/<id>', methods=['PUT'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def updateTabla(id):
        data = auto.query.get(id)
        print(data)
        # id = request.json['id']

        marca = request.json['marca']
        modelo = request.json['modelo']
        categoria = request.json['categoria']
        puertas = request.json['puertas']
        precio = request.json['precio']
        id_socio = request.json['id_socio']

        # data.id = id
        data.marca = marca
        data.modelo = modelo
        data.categoria = categoria
        data.puertas = puertas
        data.precio = precio
        data.id_socio = id_socio

        db.session.commit()
        return "OK"

    @app.route('/delAuto/<id>', methods=['DELETE'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def delete_auto(id):
        data = auto.query.get(id)
        db.session.delete(data)
        db.session.commit()
        return auto.auto_schema.jsonify(data)
