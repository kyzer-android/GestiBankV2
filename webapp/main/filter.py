import datetime

from webapp.main import bp
from flask import current_app as app

@app.template_filter('formater_date')
def formater_date(madate):
    if isinstance(madate,(datetime.datetime,datetime.date)):
        return madate.strftime("%d/%m/%Y")
    return madate


