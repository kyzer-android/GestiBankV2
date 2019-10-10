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

    # def test_lister_agent(self):
    #     test=Admin.lister_agent()
    #     logging.info("test_lister_agent_param", test[0])
    #     logging.info("test_lister_agent", test[1])
    #     # for val in test :
    #     #     logging.info("test_lister_un_agent",val)
    #
    # def test_lister_demand(self):
    #     utilisateur = Admin.query.get(1)
    #     test=utilisateur.lister_demand_crea()
    #     logging.info("lister les demande",test)

    # def test_list_demand(self):
    #     listet = Admin.Choicelist_agent()
    #     # final_list=[]
    #     logging.info(listet)
    #     # for list in listet:
    #     #     final_list.append((list['id'],list['username']))
    #
    #     # logging.info("lister les demande", final_list)

    def test_demande_crea_vide(self):
        test = Admin.lister_demande_non_affecter()
        logging.info("lister les demande", test)
        if len(test) !=0:
            logging.info("liste vide")
        else :
            logging.info("pas vide")


if __name__ == "__main__":
    unittest.main()