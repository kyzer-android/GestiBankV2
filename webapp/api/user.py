from flask import jsonify, request, url_for, flash
from flask_babel import lazy_gettext as _l
from werkzeug.utils import redirect

from webapp import db
from webapp.api import bp
from webapp.main.models import User, Post


@bp.route('/users/<int:id>', methods=['GET'])
@bp.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    return jsonify((User.query.get_or_404(id, _l("User %(id)s is not found ", id=id))).to_dict(include_email=True))


@bp.route('/users', methods=['GET'])
def get_users():
    try :
        page = int(request.args.get('page'))
    except :
        page = 1
    finally:
        if 'per_page' in request.args:
            per_page=int(request.args.get('per_page'))
        else:
            per_page=5
        return jsonify( User.to_collection_dict(query=User.query,
                                               page=page,
                                               per_page=per_page,
                                               endpoint='api.get_users'))

@bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
     return jsonify(Post.query.get_or_404(id).to_dict())


@bp.route('/users/<int:id>/posts', methods=['GET'])
def get_posts(id):
    return jsonify(Post.to_collection_dict(query=User.query.get(id).posts,
                                               page=1,
                                               per_page=10,
                                               endpoint='api.get_posts',
                                            id=id
                                           ))


@bp.route('/posts', methods=['GET'])
def get_posts_all():
    return jsonify(Post.to_collection_dict(query=Post.query,
                                           page=1,
                                           per_page=10,
                                           endpoint='api.get_posts_all'))


@bp.route('/users', methods=['POST'])
def create_user():
    this_user =User()
    this_user.from_dict(data=request.json,new_user=True)
    try:
        User.populate(this_user)
    except Exception as e:
         flash('error',e)
    return redirect(url_for('api.get_users'))


@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    this_user=User.query.get_or_404(id, _l("User %(id)s is not found ", id=id))

    if this_user is not None:
        this_user.from_dict (data=request.json)
        User.populate(this_user)

    return redirect(url_for('api.get_user',id=id))
