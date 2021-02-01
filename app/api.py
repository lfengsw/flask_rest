import uuid
from flask import jsonify
from flask import request
from flask_restful import Resource,Api,fields,marshal_with, abort, marshal
from app.model import UserModel
api = Api()

def init_api(app):
    api.init_app(app)


user_fiels= {
    "id":fields.Integer(attribute="id"),
    "name":fields.String(attribute="username"),
    "password":fields.Integer(attribute="password"),
    "token":fields.String(attribute="token"),
    "permission":fields.Float(attribute="permission"),
}

user_result_fields = {
    "list":fields.List(fields.Nested(user_fiels)),
    "extra":fields.String
}

class UserInfo(Resource):

    @marshal_with(user_result_fields)
    def get(self):
        user = UserModel.query.all()
        return {
                "list":user,
                "extra":""
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
            return jsonify({"code": 200, "msg": "error"})

api.add_resource(UserInfo,'/user/')



