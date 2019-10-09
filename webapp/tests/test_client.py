import logging
import unittest
from webapp import create_app
from webapp.gestibank.models.clients import Client
from webapp.extension import db
from webapp.gestibank.models.user import User

import logging
import unittest
from webapp import create_app
from webapp.gestibank.models.clients import Client
from webapp.extension import db
from webapp.gestibank.models.user import User

class TestUser (unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        db.session.remove()

    def teste_client(self):
        client=Client(username='chankite', password_hash=User.password('123456789'))
        db.session.add(client)
        db.session.commit()
        c1=Client.query.all()
        print(c1)

    def test_recup(self):
        clients=Client.query.filter_by(username="chankite").first()
        logging.info(clients)



class TestUser (unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        db.session.remove()

    def teste_client(self):
        client=Client(username='chankite', password_hash=User.password('123456789'))
        db.session.add(client)
        db.session.commit()
        c1=Client.query.all()
        print(c1)

    def test_recup(self):
        clients=Client.query.filter_by(username="chankite").first()
        logging.info(clients)


if __name__ == "__main__":
    unittest.main()

if __name__ == "__main__":
    unittest.main()
