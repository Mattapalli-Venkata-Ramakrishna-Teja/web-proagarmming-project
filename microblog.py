from app import app, db
from app.models import Addbuyer, Addstock


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Addstock': Addstock, 'Addbuyer': Addbuyer}
