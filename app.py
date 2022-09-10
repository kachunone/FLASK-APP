from flask import Flask, request
app = Flask(__name__)

@app.route("/test")
def home():
    return "This is a test string"

@app.route("/search")
def search():
    problemType = request.args.get('type')
    return problemType;

if __name__ == '__main__':
    app.run()