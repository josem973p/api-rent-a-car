from auto import *
from socio import *
from cliente import *
from disponibilidad import *
from reservaciones import *



if __name__ == "__main__":

    db.create_all()

    app.run(debug=True)