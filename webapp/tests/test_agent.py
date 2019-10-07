import unittest
from webapp import create_app
from webapp.gestibank.models.agents import Agent
from webapp.extension import db


class TestUser (unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()





    def tearDown(self):
        db.session.remove()

    def test_listdemandecrea(self):
        agent = Agent.query.get(3)

        list= agent.filtre_compte()
        print(list)



if __name__ == "__main__":
    unittest.main()