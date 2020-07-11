from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<br><br>Hello World!<br><br>NES START!"

if __name__ == "__main__":
    app.run()
