from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

counter = 0  # глобальна змінна (пізніше можна замінити на Redis/БД)

@app.route("/")
def index():
    return render_template("index.html", count=counter)

@app.route("/increment", methods=["POST"])
def increment():
    global counter
    counter += 1
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
