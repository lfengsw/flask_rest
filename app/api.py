import json
import uuid
from flask import jsonify
from flask import request
from flask_restful import Resource,Api,fields,marshal_with, abort, marshal
from app.model import UserModel, City

api = Api()

def init_api(app):
    api.init_app(app)

class UserInfo(Resource):


    #@marshal_with(user_result_fields)
    def get(self,id):

        city_fields = {
           "id": fields.Integer(attribute="id"),
            "name": fields.String(attribute="regionName"),
            "code": fields.String(attribute="cityCode"),
        }
        city = City.query.get(id)
        city_info=json.loads(json.dumps(marshal(city, city_fields)))
        user_fields = {
            "id": fields.Integer(attribute="id"),
            "name": fields.String(attribute="username"),
            "password": fields.String(attribute="password"),
            "token": fields.String(attribute="token"),
            "permission": fields.Float(attribute="permission"),
            "city_info":fields.String(city_info)

        }

        # user_result_fields = {
        #     "list": fields.List(fields.Nested(user_fields)),
        #     "extra": fields.String
        # }

        user = UserModel.query.get(id)
        return {
                "list":marshal(user,user_fields),
                "code":200,
        }

    def post(self):
        name = request.form.get('name')
        password = request.form.get('password')
        token= str(uuid.uuid4().hex)
        user = UserModel()
        if not  user.query.filter_by(username=name).count():
            user.username = name
            user.password = password
            user.token = token
            if user.save():
                return jsonify({"code":200,"msg":"success","token":token})
        else:
            return jsonify({"code": 200, "msg": "添加失败"})

api.add_resource(UserInfo,'/user/','/user/<int:id>')



