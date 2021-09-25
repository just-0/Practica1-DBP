from flask import Flask # Import the class `Flask` from the `flask` module, written by someone else.

app = Flask(__name__) # Instantiate a new web application called `app`, with `__name__` representing the current file


@app.route("/")
def index():
    return f"poner 3 valores en el url /a/b/c"

@app.route("/<int:a>/<int:b>/<int:c>")
def sin_nombre(a,b,c):
    return f"La fecha es: {a}/{b}/{c} "
