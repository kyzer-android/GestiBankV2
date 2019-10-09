import logging
import unittest
from webapp import create_app
from webapp.gestibank.models.admin import Admin
from webapp.extension import db


class TestUser (unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        db.session.remove()

    def test_lister_agent(self):
        test=Admin.lister_agent()
        logging.info("test_lister_agent", test)
        for val in test :
            logging.info("test_lister_agent",val)

    def test_lister_demand(self):
        utilisateur = Admin.query.get(1)
        test=utilisateur.lister_demand_crea()
        logging.info("lister les demande",test)


if __name__ == "__main__":
    unittest.main()