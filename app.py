from flask import Flask
app = Flask(__name__)

@app.route("/test")
def home():
    return "OK! You reach me!"

if __name__ == '__main__':
    app.run()