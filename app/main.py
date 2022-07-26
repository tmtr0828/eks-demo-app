import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello World from {os.environ.get('ENV')}!!"

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)