from flask_restful import Api
from app.api import UserInfo, AddressResource
from app.model import UserModel,Letter,City
from app.ext import api
api.add_resource(UserInfo,'/user/','/user/<int:id>')
api.add_resource(AddressResource,'/address/','/address/<int:id>')