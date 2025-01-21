from flask import Flask, render_template

app = Flask(__name__)

# נתיב לדף הראשי - שאלות ותשובות
@app.route('/')
def questions():
    return render_template("questions.html")

# נתיב לדף index הראשי (אם תרצה לשמור אותו)
@app.route('/home')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
