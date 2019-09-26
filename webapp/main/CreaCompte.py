from webapp.main.models import User
from webapp.extension import db



class DemandeCreacompte(db.Model):
    id_compte = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(120))
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    mail = db.Column(db.String(50))
    tel = db.Column(db.String(20))
    adresse = db.Column(db.String(140))
    justificatif = db.Column(db.String(20))
    affect = db.Column(db.String(50))
    valide = db.Column(db.Boolean)

    def __repr__(self):
        test = (
            self.id,
            self.username,
            self.password,
            self.nom,
            self.prenom,
            self.mail,
            self.tel,
            self.adresse,
            self.justificatif,
            self.valid,
            self.affect
        )
        return str(test)

    def affectation(self, agent):  # l'admin affect un client a un agent
        self.affect = agent
        db.session.commit(self)
        db.session.close()

    def validation(self, valide):  # L'agent valide le client
        self.valide = valide
        db.session.commit(self)
        db.session.close()



def add_demande(formulaire):  # Stocakge d'une demmande dans la base de donnee (table demande)
    demande = DemandeCreacompte(

        username=formulaire.username.data,
        nom=formulaire.nom.data,
        prenom=formulaire.prenom.data,
        password=User.password(formulaire.password.data),
        mail=formulaire.mail.data,
        tel=formulaire.tel.data,
        adresse=formulaire.adresse.data,
        justificatif=formulaire.justificatif.data
    )

    User.populate(demande)
