import logging
import unittest
from webapp import create_app
from webapp.gestibank.models.admin import Admin
from webapp.extension import db

def peuplement():
    app = create_app()
    app_context = app.app_context()
    app_context.push()

    admin=Admin(nom='durant',prenom='pierre',)



if __name__ == "__main__":
    peuplement()