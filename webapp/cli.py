import os
import click
#Module de définition des differentes fonction utilisable depuis le
# terminal pour facilité l'utilisation et l'exportation du logiciel

def register(app):
    @app.cli.group()
    def translate():
        """Translation and localization commands."""
        pass

    @app.cli.group()
    def Servermail():
        """Server Mail"""
        pass

    @translate.command()
    def update():
        """Update all languages."""
        if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
            raise RuntimeError('extract command failed')
        if os.system('pybabel update -i messages.pot -d webapp/translations'):
            raise RuntimeError('update command failed')
        os.remove('messages.pot')

    @translate.command()
    def compile():
        """Compile all languages."""
        if os.system('pybabel compile -d webapp/translations'):
            raise RuntimeError('compile command failed')

    @translate.command()
    @click.argument('lang')
    def init(lang):
        """Initialize a new language."""
        if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
            raise RuntimeError('extract command failed')
        if os.system(
                'pybabel init -i messages.pot -d webapp/translations -l ' + lang):
            raise RuntimeError('init command failed')
        os.remove('messages.pot')

    @Servermail.command()
    def run():
        if os.system('python -m smtpd -n -c DebuggingServer 127.0.0.1:8025'):
            raise RuntimeError('extract command failed')