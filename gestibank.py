from webapp import create_app, cli

#Creation  et execution de l'application
app = create_app()
cli.register(app)




