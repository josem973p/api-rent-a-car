from flask_cors import CORS,cross_origin
class DatabaseConn():
    def __init__(self,app):
        app.config[
            'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:gswc789qad@localhost/rent_a_car'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['CORS_HEADERS'] = 'Content-Type'
        cors = CORS(app, resources={r"/": {"origins": "http://localhost:port"}})