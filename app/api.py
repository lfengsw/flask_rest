import json
import uuid
from flask import jsonify
from flask import request
from flask_restful import Resource,fields, abort, marshal
from flask_restful import reqparse
from sqlalchemy import and_

from app.ext import db
from app.model import UserModel, City, AddressModel


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
        if not user:
            abort(404,msg="该用户不存在",code=400)
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



class AddressResource(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('uid', type=int, required=True, help="请绑定用户信息",location=['headers','form'])
        parser.add_argument('detail', type=str, required=True, help='请输入地址信息',location=['headers','form'])
        args = parser.parse_args()
        uid = args.get('uid')
        detail = args.get('detail')
        address  = AddressModel()
        address.uid = uid
        address.detail = detail
        if not address.save():
            abort(401, msg='error')
        return jsonify({"code":200,"msg":"success"})

    def get(self,id):

        result= db.session.execute("select * from address where id ='%d'"%(id))
        new_result = list(result)
        if not new_result:
            abort(401,code=401,msg="参数错误")
        data = new_result[0]

        query=db.session.query(AddressModel.uid).outerjoin(UserModel,UserModel.id == AddressModel.uid)
        print(query)

        return jsonify({
            "code":200,
            "msg":"success",
            "data":{
                "id":data[0],
                "uid":data[1],
                "detail":data[2]
            }
        })


