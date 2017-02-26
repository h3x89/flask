"""hello.py."""

from flask import Flask             # """Main Framework"""
from flask import url_for           # """Test function"""
from flask import request           # """GET and POST"""
from flask import render_template   # """HTTP Templates"""
from flask import redirect          # """Redirection"""
from flask import abort             # """Errors"""

"""First Hello World app in Flask."""
"""Author: h3x89"""


app = Flask(__name__)


@app.route("/")
def hello():
    """Hello World."""
    return "Hello World!"


@app.route('/robert')
def robert():
    """Hi Robert."""
    return 'Hi Robert'


@app.route('/user/<username>')
def username(username):
    """Hi USERNAME."""
    """Possible to put strin and int"""
    return ('Hi %s' % username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    """Post ID."""
    """Only int"""
    return('Post %d' % post_id)

###############################################################################


@app.route('/error')
def error():
    """Error function."""
    abort(401)
    print 'error'


@app.route('/pass/<my_pass>')
def my_pass(my_pass):
    """Pass test."""
    if my_pass != 'secretpass':
        return error()
    else:
        return redirect(url_for('username', username=my_pass))

###############################################################################


@app.route('/login', methods=['GET', 'POST'])
def login():
    """GET and POST."""
    def do_the_login():
        """Test login."""
        return 'do the login return'

    def show_the_login_form():
        """Test login form."""
        return 'show the login form return'

    if request.method == 'GET':
        answer = do_the_login()
    else:
        answer = show_the_login_form()
    return ("answer is: %s" % answer)


###############################################################################


@app.route('/templates/')
@app.route('/templates/<name>')
def templates(name=None):
    """HTTP Templates."""
    return render_template('hello.html', name=name)


@app.route('/redirection')
def redirection():
    """Redirection."""
    return redirect(url_for('login'))

###############################################################################


@app.route('/result')
def result():
    """More adventages templates."""
    dict = {'phy': 50, 'che': 60, 'maths': 70}
    return render_template('result.html', result=dict)


###############################################################################


@app.route("/static")
def index():
    """Static files."""
    return render_template("index.html")


###############################################################################


with app.test_request_context():
    """Test function"""
    print url_for('hello')
    print url_for('robert')
    print url_for('username', username='John')
    print url_for('show_post', post_id=12)
    '''WRONG REQUEST - just for tests'''
    # print url_for('username')
    # print url_for('username', next='/')
    # print url_for('show_post')
    # print url_for('show_post', post_id='test')

###############################################################################


# app.route(rule, options)
# app.run(host, port, debug, options)

###############################################################################

if __name__ == "__main__":
    # app.run()
    # app.run(host, port, debug, options)
    app.run(host="0.0.0.0", port=5000, debug=True)
