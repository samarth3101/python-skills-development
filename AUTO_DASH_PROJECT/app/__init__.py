from flask import Flask

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Needed for flash messages

from app import routes  # <-- important! must come after `app = Flask(...)`