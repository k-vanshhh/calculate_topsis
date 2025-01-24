from flask import Flask
from flask_mail import Mail

def create_app():
    app = Flask(__name__)

    # Configuration settings
    app.config['UPLOAD_FOLDER'] = 'static/uploads'
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'your_email@gmail.com'  # Replace with your email
    app.config['MAIL_PASSWORD'] = 'your_password'         # Replace with your email password
    app.config['SECRET_KEY'] = 'your_secret_key'

    mail = Mail(app)

    # Register routes
    from .routes import main
    app.register_blueprint(main)

    return app