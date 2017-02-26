"""Flask - Sending Form Data to Template using cookie and sessions."""

from flask import Flask, render_template, request, make_response, redirect, url_for
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


@app.route('/cookie')
def cookie():
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
    return '<h1>welcome ' + name + '</h1>'


"""SESSION"""

@app.route('/session_login')
def session_login():
    """Session login example."""
    session['username'] = 'admin'
    # return str(session)
    return redirect(url_for('session'))


@app.route('/session_logout')
def session_logout():
    """Session logout example."""
    if 'username' in session:
        session.pop('username')
    # return str(session)
    return redirect(url_for('session'))


@app.route('/')
def index():
    """Session example."""
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/login'></b>" + "click here to log in</b></a>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login."""
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
        # return login
    return '''
    <html>

    <body>
    <form action = "login" method="POST">
        <p>username <input type="text" name="username" /></p>
        <p><input type="submit" value="submit" /></p>
    </form>

   </body>

   </html>
   '''


@app.route('/logout')
def logout():
    """Logout."""
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    session = {}
    app.secret_key = 'asdasdas'
    app.run(debug=True)
