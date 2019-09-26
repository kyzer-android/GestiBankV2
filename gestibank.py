from webapp import create_app, cli
app = create_app()
cli.register(app)


from webapp import db
from webapp.main.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}



