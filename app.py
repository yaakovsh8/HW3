from flask import Flask, render_template

app = Flask(__name__)

# דף השאלות והתשובות כעמוד הראשי
@app.route('/')
def questions():
    return render_template("questions.html")

# דף עם הקישורים לשאלות ותשובות ולגיט
@app.route('/home')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
