from flask import Flask

import models
from extensions import db

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='dev',
    SQLALCHEMY_DATABASE_URI='sqlite:////tmp/test.db'
)

# init exts
db.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
