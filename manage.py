from flask import Flask
from app.setting import config
from flask_script import Manager
from flask_migrate import MigrateCommand
from app.ext import init_ext
from app.api import init_api
app = Flask(__name__)

app.config.from_object(config['test'])
manager = Manager(app)
manager.add_command('db',MigrateCommand)
init_ext(app)
init_api(app)

if __name__ == "__main__":
    manager.run()

