from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app(CORS)


@app.route("/theApp")
def sayHi():
    print("Hi from Python")
    return

if __name__ == "__main__":
    port = 8000
    app.run(host="0.0.0.0",port=port)