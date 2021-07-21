from flask import Flask
from hello import *

app = Flask(__name__)
app.add_url_rule('/', 'index', say_hello)

if __name__ == "__main__":
    # app.debug = True
    app.run(host='0.0.0.0', port=80)

#  pylama:ignore=D100,D103
