from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "hi"


if __name__ == "__name__":
    print("Starting python flask server for real estate price prediction of Bengaluru...")
    app.run()
