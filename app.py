from flask import Flask, render_template, request

app = Flask(__name__)

def check_strength(password):
    if len(password) < 6:
        return "Weak"
    elif password.isalpha() or password.isdigit():
        return "Medium"
    else:
        return "Strong"

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        password = request.form["password"]
        result = check_strength(password)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)