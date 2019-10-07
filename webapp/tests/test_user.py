import unittest
from webapp import create_app
from webapp.gestibank.models import User
from webapp.extension import db


class TestUser (unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()





    def tearDown(self):
        db.session.remove()

    def test_lister_user(self):
        print("test")
        utilisateur= User.query.get(1)
        print(utilisateur)


if __name__ == "__main__":
    unittest.main()