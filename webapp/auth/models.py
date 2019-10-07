from flask import current_app
from flask_login import current_user
from functools import wraps


#Decorateur verifiant que le compte utiliser est du type admin
def login_admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.type == 'admin':
            return func(*args, **kwargs)
        else:
            return current_app.login_manager.unauthorized()
    return decorated_view

#Decorateur verifiant que le compte utiliser est du type Agent
def login_agent_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.type == 'agent':
            return func(*args, **kwargs)
        else:
            return current_app.login_manager.unauthorized()
    return decorated_view

#Decorateur verifiant que le compte utiliser est du type Client
def login_client_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.type == 'client':
            return func(*args, **kwargs)
        else:
            return current_app.login_manager.unauthorized()
    return decorated_view
