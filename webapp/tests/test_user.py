import unittest

import logging

from webapp import create_app
from webapp.gestibank.models.agents import Agent
from webapp.gestibank.models.user import User
from webapp.extension import db
logging.basicConfig(level=logging.DEBUG)

class TestUser (unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()





    def tearDown(self):
        db.session.remove()

    #test lister les demande de compte
    def test_lister_user(self):
        utilisateur= User.query.get(1)
        logging.debug(utilisateur)
        logging.debug(utilisateur.lister_demand_crea())

    #test affectation d'une demande
    def test_affecter_demande(self):
        utilisateur= User.query.get(1)
        demande=utilisateur.lister_demand_crea()[0]
        utilisateur.affecter_demande(demande,1)
        logging.debug(utilisateur.lister_demand_crea()[0])

    def test_lister_agent(self):
        pass


if __name__ == "__main__":
    unittest.main()