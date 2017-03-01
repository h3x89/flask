"""Sqlite and Flask."""
from flask import Flask, render_template, request, url_for, redirect
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
   return render_template('home.html')


@app.route('/enternew')
def new_student():
    """Function which render student temlate."""
    return render_template('student3.html')


# @app.route('/addrec', methods=['POST', 'GET'])
# def addrec():
#     if request.method == 'POST':
#         try:
#             nm = request.form['nm']
#             addr = request.form['add']
#             city = request.form['city']
#             pin = request.form['pin']
#
#             with sqlite3.connect("database.db") as con:
#                 cur = con.cursor()
#                 cur.execute("INSERT INTO students(name, addr, city, pin) \
#                             VALUES(?, ?, ?, ?)", (nm, addr, city, pin))
#
#                 con.commit()
#                 msg = "Record successfully added"
#         except:
#             con.rollback()
#             msg = "error in insert operation"
#
#         finally:
#             return render_template("result3.html", msg=msg)
#             con.close()


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    """Function without try:."""
    if request.method == 'POST':
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            con = sqlite3.connect("database/database.db")
            try:
                con.execute("CREATE TABLE students \
                (name TXT, addr TXT, city TXT, pin TXT)")
            except:
                print("execute")

            cur = con.cursor()
            cur.execute("INSERT INTO students(name, addr, city, pin) \
                        VALUES(?, ?, ?, ?)", (nm, addr, city, pin))

            con.commit()
            msg = "Record successfully added"

            return render_template("result3.html", msg=msg)
            con.close()


@app.route('/list')
def list():
    """List elements."""
    con = sqlite3.connect("database/database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall()
    return render_template("list.html", rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
