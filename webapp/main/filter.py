import datetime
from webapp.main import bp

#filtre de transformation de date au norme francaise
@bp.app_template_filter('formater_date2')
def formater_date2(madate):
    if isinstance(madate,(datetime.datetime,datetime.date)):
        return madate.strftime("%d/%m/%Y")
    return madate