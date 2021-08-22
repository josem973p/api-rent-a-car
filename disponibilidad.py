import sqlalchemy
from flask import request, jsonify
from start import *
from sqlalchemy.exc import *
from flask_cors import CORS, cross_origin


class disponibilidad(db.Model):
    id_disponibilidad = db.Column(db.Integer, primary_key=True)
    id_auto = db.Column(db.Integer)
    en_uso = db.Column(db.Integer)



    def __init__(self, id_auto, en_uso):
        self.id_auto = id_auto
        self.en_uso = en_uso


    db.create_all()

    class disponibleSchema(ma.Schema):

        class Meta:
            fields = ('id_disponibilidad', 'id_auto', 'en_uso')

    disponible_Schema = disponibleSchema()
    disponibles_schema = disponibleSchema(many=True)

    @app.route('/getDisponibles', methods=['GET'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def disponible_data():
        data = disponibilidad.query.all()
        result = disponibilidad.disponibles_schema.dump(data)
        return jsonify(result)

    @app.route('/getDisponibleBy/<id>', methods=['GET'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def get_disponibleBy(id):
        data = disponibilidad.query.get(id)
        if data == None:
            return "Not mach found"
        return disponibilidad.disponible_Schema.jsonify(data)

    @app.route('/addDisponibles', methods=['POST'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def adddisponible():
        # id = request.json['id']
        id_auto = request.json['id_auto']
        en_uso = request.json['en_uso']

        newdisponible = disponibilidad(id_auto, en_uso)

        db.session.add(newdisponible)
        db.session.commit()
        return "OK"

    @app.route('/UpdateDisponible/<id>', methods=['PUT'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def updateDisponible(id):
        data = disponibilidad.query.get(id)
        print(data)
        # id = request.json['id']

        id_auto = request.json['id_auto']
        en_uso = request.json['en_uso']


        # data.id = id

        data.id_auto = id_auto
        data.en_uso = en_uso

        db.session.commit()
        return "OK"

    @app.route('/delDisponible/<id>', methods=['DELETE'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def delete_disponible(id):
        data = disponibilidad.query.get(id)
        db.session.delete(data)
        db.session.commit()
        return disponibilidad.disponible_Schema.jsonify(data)
