from flask import Flask 
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

from config import Config
from models.questions_model import db
from routes.db_routes import qa_bp
from routes.general_routes import general_bp



# print(f"SQLALCHEMY_DATABASE_URI: {os.getenv('SQLALCHEMY_DATABASE_URI')}")
# print(f"OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY')}")

app = Flask(__name__)

#Load configurations
app.config.from_object(Config)

print(f"Loaded Config SQLALCHEMY_DATABASE_URI: {app.config['SQLALCHEMY_DATABASE_URI']}")


# Initialize the database with the app
db.init_app(app)

# Create the database
with app.app_context():
    db.create_all()

# Register blueprints (for routes)
app.register_blueprint(qa_bp)
app.register_blueprint(general_bp, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)