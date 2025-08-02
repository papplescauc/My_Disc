from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_view():
    return render_template('index.html')

@app.route('/courses')
def courses_view():
    return 'Course Page'

@app.route('/login')
def login_view():
    return render_template('login.html')



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)