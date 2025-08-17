from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_view():
    return render_template('index.html')

@app.route('/courses')
def courses_view():
    return render_template('courses.html')

@app.route('/courses/add')
def add_course_view():
    
    return render_template('add_course.html')

@app.route('/current_round')
def current_round_view():
    return render_template('current_round.html')

@app.route('/login')
def login_view():
    return render_template('login.html')

@app.route('/python_function/')
def python_function():
    print('yooooo we did a thing')
    1/0
    return {'data': 'this is the data'}

@app.errorhandler(Exception)
def error_handler(err: Exception):
    response = {
        'error': err.__class__.__name__,
        'message': str(err)
    }
    return response, 500


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=False)