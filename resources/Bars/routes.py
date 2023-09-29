from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity

from resources.users.models import UserModel

from .BarModel import BarModel
from schemas import BarSchema
from . import bp


@bp.route('/')
class PostList(MethodView):
  
  @jwt_required()
  @bp.response(200, BarSchema(many=True))
  def get(self):
    return BarModel.query.all()

  @jwt_required()
  @bp.arguments(BarSchema)
  @bp.response(200, BarSchema)
  def post(self, bars_data):
    user_id = get_jwt_identity()
    p = BarModel(**bars_data, user_id = user_id)
    try:
      p.save()
      return p
    except IntegrityError:
      abort(400, message="Invalid User Id")

@bp.route('/<post_id>')
class Post(MethodView):
  
  @jwt_required()
  @bp.response(200, BarSchema)
  def get(self, bars_id):
    p = BarModel.query.get(bars_id)
    if p:
      return p
    abort(400, message='Invalid Post Id')

  @jwt_required()
  @bp.arguments(BarSchema)
  @bp.response(200, BarSchema)
  def put(self, bars_data, bars_id):
    p = BarModel.query.get(bars_id)
    if p and bars_data['name']:
      user_id = get_jwt_identity()
      if p.user_id == user_id:
        p.body = bars_data['name']
        p.save()
        return p
      else:
        abort(401, message='Unauthorized')
    abort(400, message='Invalid Bar Data')

  @jwt_required()
  def delete(self, bars_id):
     user_id = get_jwt_identity()
     p = BarModel.query.get(bars_id)
     if p:
       if p.user_id == user_id:
        p.delete()
        return {'message' : 'Bar Deleted'}, 202
       abort(401, message='User doesn\'t have rights')
     abort(400, message='Invalid Bar Id')
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  @bp.response(200, BarSchema(many=True))
  def get(self):
    return BarModel.query.all()

  @bp.arguments(BarSchema)
  @bp.response(200, BarSchema)
  def post(self, bar_data):
    p = BarModel(**bar_data)
    u = UserModel.query.get(bar_data['user_id'])
    if u:
      p.save()
      return p
    else:
      abort(400, message="Invalid User Id")

@bp.route('/<bars_id>')
class Post(MethodView):
  
  @bp.response(200, BarSchema)
  def get(self, post_id):
    p = BarModel.query.get(post_id)
    if p:
      return p
    abort(400, message='Invalid Post Id')

  @bp.arguments(BarSchema)
  @bp.response(200, BarSchema)
  def put(self, post_data, post_id):
    p = BarModel.query.get(post_id)
    if p and post_data['name']:
      if p.user_id == post_data['user_id']:
        p.body = post_data['name']
        p.save()
        return p
    abort(400, message='Invalid Bar Data')

  def delete(self, bar_id):
     req_data = request.get_json()
     user_id = req_data['user_id']
     p = BarModel.query.get(bar_id)
     if p:
       if p.user_id == user_id:
        p.delete()
        return {'message' : 'Bar Deleted'}, 202
       abort(400, message='User doesn\'t have rights')
     abort(400, message='Invalid Post Id')