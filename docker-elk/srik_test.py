from app import app
from app.models import Person

@app.shell_context_processor
def make_shell_context():
  return {'app':app, 'Person': Person}
