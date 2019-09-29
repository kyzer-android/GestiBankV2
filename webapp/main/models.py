# from datetime import datetime
# from time import time
# from flask import flash, url_for, current_app
# from flask_login import UserMixin
# from werkzeug.utils import redirect
# from webapp.extension import db, login
# from werkzeug.security import generate_password_hash, check_password_hash
# import jwt
#
#
# class PaginatedAPIMixin(object):
#     @staticmethod
#     def to_collection_dict(query, page, per_page, endpoint, **kwargs):
#
#         resources = query.paginate(page, per_page, False)
#
#         data = {
#             'items': [item.to_dict() for item in resources.items],
#             '_meta': {
#                 'page': page,
#                 'per_page': per_page,
#                 'total_pages': resources.pages,
#                 'total_items': resources.total
#             },
#             '_links': {
#                 'self': url_for(endpoint, page=page, per_page=per_page, **kwargs),
#                 'next': url_for(endpoint, page=page + 1, per_page=per_page,
#                                 **kwargs) if resources.has_next else None,
#                 'prev': url_for(endpoint, page=page - 1, per_page=per_page,
#                                 **kwargs) if resources.has_prev else None
#             }
#         }
#         return data
#
#
#
#
#     def to_dict(self, include_email=False):
#         data = {
#                 'id': self.id,
#                 'username': self.username,
#                 'post_count': self.posts.count(),
#                 '_links': {
#                 'self': url_for('api.get_user', id=self.id),
#                 'posts': url_for('api.get_posts', id=self.id)
#                 }
#         }
#         if include_email:
#             data['email'] = self.email
#         return data
#
#
#
#     def from_dict(self, data, new_user=False):
#         for field in ['username', 'email']:
#             if field in data:
#                 setattr(self, field, data[field])
#             if new_user and 'password' in data:
#                 self.set_password(data['password'])
#
#
#
# class Post(PaginatedAPIMixin,db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#     def to_dict(self):
#         data = {
#                 'id': self.id,
#                 'body': self.body,
#                 'timestamp': self.timestamp,
#                 '_links': {
#                 'self': url_for('api.get_post', id=self.id),
#                 'user': url_for('api.get_user', id=self.user_id)
#                 }
#         }
#         return data
#
#
#
#     def __repr__(self):
#         return '<Post {}>'.format(self.body)
#
#
#
#
# def select_all():
#     users = User.query.all()
#     return users
#
#
#
