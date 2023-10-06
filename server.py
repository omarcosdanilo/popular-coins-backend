from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


@app.route("/inicio")
def ola():
    return "Hello World"


app.run(debug=True)
