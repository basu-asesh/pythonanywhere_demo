from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask on pythonanywhere!"

@app.route("/1")
def f1():
    return render_template("1.html")

if __name__ == "__main__":
    app.run()
