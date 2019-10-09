import unittest
from webapp import create_app
from webapp.gestibank.models.agents import Agent
from webapp.extension import db
import logging


class TestUser (unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()





    def tearDown(self):
        db.session.remove()

    def test_lister_demandecrea(self):
        agent = Agent.query.get(2)

        list= agent.lister_demandecrea()
        logging.debug(list)

    # def test_validation(self):
    #     valide = Agent.query.get(3)
    #     validation = Agent.validation_Crea(valide)
    #     print(validation)



if __name__ == "__main__":
    unittest.main()