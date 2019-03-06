from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def say_hello():
  return render_template("index.html")

@app.route("/<name>")
def say_hello_to(name):
    return f"Hello {name}"

@app.route("/qwerty")
def qwerty():
    return "qwerty"



#debug=True meens updateing the app.py here and
#saving it will automatically reload the webpage :)
app.run(debug=True)
