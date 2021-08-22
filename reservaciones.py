import sqlalchemy
from flask import  request, jsonify
from start import *
from sqlalchemy.exc import  *
from flask_cors import CORS,cross_origin

class reservaciones(db.Model):
    id_reservacion = db.Column(db.Integer, primary_key=True)
    ubi_entrega = db.Column(db.String(45))
    ubi_devol = db.Column(db.String(45))
    fecha_entrega = db.Column(db.DATE)
    fecha_devol = db.Column(db.DATE)
    id_auto = db.Column(db.Integer)
    id_socio= db.Column(db.Integer)
    precio_total = db.Column(db.DECIMAL(asdecimal=False))
    id_cliente= db.Column(db.Integer)


    def __init__(self,ubi_entrega,ubi_devol,fecha_entrega,fecha_devol,id_auto,id_socio,precio_total,id_cliente):
        self.ubi_entrega=ubi_entrega
        self.ubi_devol=ubi_devol
        self.fecha_entrega=fecha_entrega
        self.fecha_devol=fecha_devol
        self.id_auto=id_auto
        self.id_socio=id_socio
        self.precio_total = precio_total
        self.id_cliente=id_cliente

    db.create_all()

    class reservacionesSchema(ma.Schema):

        class Meta:
            fields=('id_reservacion','ubi_entrega','ubi_devol','fecha_entrega','fecha_devol','id_auto','id_socio','precio_total','id_cliente')

    reservacion_schema= reservacionesSchema()
    reservaciones_schema=reservacionesSchema(many=True)

    @app.route('/getReservaciones', methods=['GET'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def reservaciones_data():
        data = reservaciones.query.all()
        result = reservaciones.reservaciones_schema.dump(data)
        return jsonify(result)

    @app.route('/getReservacionesBy/<id>', methods=['GET'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def get_reservacionBy(id):
        data = reservaciones.query.get(id)
        if data == None:
            return "Not mach found"
        return reservaciones.reservacion_schema.jsonify(data)

    @app.route('/addReservaciones', methods=['POST'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def addreservaciones():

        # id = request.json['id']

        ubi_entrega = request.json['ubi_entrega']
        ubi_devol = request.json['ubi_devol']
        fecha_entrega = request.json['fecha_entrega']
        fecha_devol = request.json['fecha_devol']
        id_auto = request.json['id_auto']
        id_socio = request.json['id_socio']
        precio_total = request.json['precio_total']
        id_cliente = request.json['id_cliente']

        newreservaciones = reservaciones(ubi_entrega, ubi_devol, fecha_entrega, fecha_devol, id_auto,id_socio,precio_total,id_cliente)

        db.session.add(newreservaciones)
        db.session.commit()
        return "OK"

    @app.route('/updateReservaciones/<id>', methods=['PUT'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def updatereservaciones(id):
        data = reservaciones.query.get(id)
        print(data)
        # id = request.json['id']
        fields = ('id_reservacion', 'ubi_entrega', 'ubi_devol', 'fecha_entrega', 'fecha_devol', 'id_auto', 'id_socio',
                  'precio_total', 'id_cliente')

        ubi_entrega = request.json['ubi_entrega']
        ubi_devol = request.json['ubi_devol']
        fecha_entrega = request.json['fecha_entrega']
        fecha_devol = request.json['fecha_devol']
        id_auto = request.json['id_auto']
        id_socio = request.json['id_socio']
        precio_total = request.json['precio_total']
        id_cliente = request.json['id_cliente']


        # data.id = id

        data.ubi_entrega = ubi_entrega
        data.ubi_devol = ubi_devol
        data.fecha_entrega = fecha_entrega
        data.fecha_devol = fecha_devol
        data.id_auto = id_auto
        data.id_socio = id_socio
        data.precio_total = precio_total
        data.id_cliente = id_cliente

        db.session.commit()
        return "OK"

    @app.route('/reservacionesDel/<id>', methods=['DELETE'])
    @cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
    def delete_reservaciones(id):
        data = reservaciones.query.get(id)
        db.session.delete(data)
        db.session.commit()
        return reservaciones.reservacion_schema.jsonify(data)