import datetime

from webapp.main import bp
from flask import current_app as app

@app.template_filter('formater_date')
def formater_date(madate):
    if isinstance(madate,(datetime.datetime,datetime.date)):
        return madate.strftime("%d/%m/%Y")
    return madate

@bp.app_template_filter('formater_date2')
def formater_date2(madate):
    if isinstance(madate,(datetime.datetime,datetime.date)):
        return madate.strftime("%d/%m/%Y")
    return madate
 ## Deux methodepour faire la meme chose bp.app_template_filter et le decorateur des filtre d'un blueprint
 ## quand a aap.temple.filtre il n'est utilisable que pasrque dans le _init__ general j'ai defint un
# " with app.app_context():
#  import main.fliter
## integrant au context les filtres.
