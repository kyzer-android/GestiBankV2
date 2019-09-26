import enum
from webapp import db

from werkzeug.security import generate_password_hash, check_password_hash

class TypeUser(enum.Enum):
    ADMIN='admin'
    AGENT='agent'
    CLIENT='client'






def set_pwd(self, pwd):
    self.password = generate_password_hash(pwd)

def check_pwd(self, pwd):
    return check_password_hash(self.password_hash, pwd)
