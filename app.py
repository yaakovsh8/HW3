from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page (index.html)
@app.route("/")
def home():
    return render_template("index.html")

# Route for the questions page (questions.html)
@app.route("/questions")
def questions():
    return render_template("questions.html")

if __name__ == "__main__":
    app.run(debug=True)
