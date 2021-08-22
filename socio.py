import sqlalchemy
from flask import request, jsonify
from start import *
from sqlalchemy.exc import *
from flask_cors import CORS, cross_origin


class socios(db.Model):
    id_socio = db.Column(db.Integer, primary_key=True)
    nombre_socio = db.Column(db.String(45))
    apellido_socio = db.Column(db.String(45))
    edad_socio = db.Column(db.Integer)
    identificacion_socio = db.Column(db.String(45))

    def __init__(self, nombre_socio, apellido_socio, edad_socio, identificacion_socio):
        self.nombre_socio = nombre_socio
        self.apellido_socio = apellido_socio
        self.edad_socio = edad_socio
        self.identificacion_socio = identificacion_socio

    db.create_all()

    class socioSchema(ma.Schema):
        class Meta:
            fields = ('id_socio', 'nombre_socio', 'apellido_socio', 'edad_socio', 'identificacion_socio')

    socio_schema = socioSchema()
    socios_schema = socioSchema(many=True)

    @app.route('/getSocios', methods=['GET'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def socio_data():
        data = socios.query.all()
        result = socios.socios_schema.dump(data)
        print(data)
        return jsonify(result)


    @app.route('/getSocioBy/<id>', methods=['GET'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def get_socioBy(id):
        data = socios.query.get(id)
        if data == None:
            return "Not mach found"
        return socios.socio_schema.jsonify(data)

    @app.route('/addSocio', methods=['POST'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def addsocio():
        # id = request.json['id']
        nombre_socio = request.json['nombre_socio']
        apellido_socio = request.json['apellido_socio']
        edad_socio = request.json['edad_socio']
        identificacion_socio = request.json['identificacion_socio']

        newcliente = socios(nombre_socio, apellido_socio, edad_socio, identificacion_socio)

        db.session.add(newcliente)
        db.session.commit()
        return "OK"

    @app.route('/updateSocio/<id>', methods=['PUT'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def updateSocio(id):
        data = socios.query.get(id)
        print(data)
        # id = request.json['id']

        nombre_socio = request.json['nombre_socio']
        apellido_socio = request.json['apellido_socio']
        edad_socio = request.json['edad_socio']
        identificacion_socio = request.json['identificacion_socio']


        # data.id = id

        data.nombre_socio = nombre_socio
        data.apellido_socio = apellido_socio
        data.edad_socio = edad_socio
        data.identificacion_socio = identificacion_socio


        db.session.commit()
        return "OK"

    @app.route('/socioDel/<id>', methods=['DELETE'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def delete_socio(id):
        data = socios.query.get(id)
        db.session.delete(data)
        db.session.commit()
        return socios.socio_schema.jsonify(data)




