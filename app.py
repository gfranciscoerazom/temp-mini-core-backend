# from controllers.notificacion_controller import notificacion_blueprint
# from controllers.signimages_controller import sign_images_blueprint
# from controllers.color_publicacion_controller import color_publicacion_blueprint
from controllers.publicacion_controller import publicacion_blueprint
# from controllers.usuario_controller import user_blueprint
# from controllers.raza_controller import raza_blueprint
# from controllers.especie_controller import especie_blueprint
# from controllers.ciudad_controller import ciudad_blueprint
# from controllers.provincia_controller import provincia_blueprint
from utils.database import db
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Database configuration
# Replace with your actual Google Cloud SQL credentials
db_path = 'sqlite:///database.db'

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
# app.config['UPLOAD_FOLDER'] = r'D:\STRAYS Final\StraysMicroservice\postImages'
CORS(app)  # Middleware for interacting with your React serve

db.init_app(app)
with app.app_context():
    db.create_all()
# Blueprint registration:

# Import the provincia_blueprint
# app.register_blueprint(provincia_blueprint)

# Import the ciudad blueprint
# app.register_blueprint(ciudad_blueprint)

# Import the especie blueprint
# app.register_blueprint(especie_blueprint)

# Import the raza blueprint
# app.register_blueprint(raza_blueprint)

# Import the usuario blueprint
# app.register_blueprint(user_blueprint)

# Import the publicacion blueprint
app.register_blueprint(publicacion_blueprint)

# Import the color_publicacion blueprint
# app.register_blueprint(color_publicacion_blueprint)

# Import the sign_images_blueprint blueprint
# app.register_blueprint(sign_images_blueprint)

# Import the notificaciones blueprint
# app.register_blueprint(notificacion_blueprint)

if __name__ == "__main__":
    app.run(
        port="0.0.0.0",
    )
