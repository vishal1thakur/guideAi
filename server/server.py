from flask import Flask
from api import api as mainBlueprint


# app instance
app = Flask(__name__)
app.register_blueprint(mainBlueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
