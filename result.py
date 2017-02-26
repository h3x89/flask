"""Flask - Sending Form Data to Template."""

from flask import Flask, render_template, request, make_response
app = Flask(__name__)


@app.route('/student')
def student():
    """Main function."""
    return render_template('student.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    """Grab form from student.html and send to result.html."""
    if request.method == 'POST':
        result = request.form
        return render_template("result2.html", result=result)
    else:
        # result = str(request.args.get)
        """why does not work?."""
        result = dict(request.args.get)
        return render_template("result2.html", result=result)


"""COOKIE"""


@app.route('/')
def index():
    """Fist cookie."""
    return render_template('cookie.html')


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    """Function to set cookie."""
    if request.method == 'POST':
        user = request.form['nm']

    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userID', user)

    return resp


@app.route('/getcookie')
def getcookie():
    """GET COOKIE."""
    name = request.cookies.get('userID')
    return '<h1>welcome '+name+'</h1>'


if __name__ == '__main__':
    app.run(debug=True)
