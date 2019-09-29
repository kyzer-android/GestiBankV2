from flask import current_app
from flask_login import current_user
from functools import wraps



def login_admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.type == 'admin':
            return func(*args, **kwargs)
        else:
            return current_app.login_manager.unauthorized()
    return decorated_view


def login_agent_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.type == 'agent':
            return func(*args, **kwargs)
        else:
            return current_app.login_manager.unauthorized()
    return decorated_view


def login_client_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.type == 'client':
            return func(*args, **kwargs)
        else:
            return current_app.login_manager.unauthorized()
    return decorated_view
