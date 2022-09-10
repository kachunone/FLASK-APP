from flask import Flask
app = Flask(__name__)

@app.route("/test")
def home():
    return "This is a test string"

@app.route("/search")
def search():
    return "This is a json format result"

if __name__ == '__main__':
    app.run()