import logging
import os
import unittest

from sqlalchemy import desc, asc

from webapp import create_app
from webapp.gestibank.models.CompteBancaire import Comptes
from webapp.extension import db
from webapp.gestibank.models.transaction import Transaction
import matplotlib.pyplot as plt


class TestUser (unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        db.session.remove()



    def test_lister_transaction(self):
        compte=Comptes.query.filter_by(id_compte=2391211101).first()
        compte.graph_transaction()



if __name__ == "__main__":
    unittest.main()