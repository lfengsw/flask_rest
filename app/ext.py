from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

db = SQLAlchemy()
migrate = Migrate()
api = Api()

def init_ext(app):
    db.init_app(app)
    migrate.init_app(app,db)
    api.init_app(app)

