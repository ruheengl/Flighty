from flask import Flask
from flaskext.mysql import MySQL
from flask import Flask, request, render_template, jsonify, redirect, url_for, session, flash
from werkzeug.security import check_password_hash, generate_password_hash


mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'riley'
app.config['MYSQL_DATABASE_PASSWORD'] = 'riley'
app.config['MYSQL_DATABASE_DB'] = 'flight'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config.update(SECRET_KEY = 'dev')
mysql.init_app(app)
conn = mysql.connect()
if conn:
    cursor = conn.cursor()


@app.route("/login",  methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # if (request.form['input_uname'] != 'admin') or (request.form['input_passwd'] != 'admin'):
        #     error = 'Invalid Credentials. Please try again.'
        #     return render_template('login.html', error = error)
        username = str(request.form['input_uname'])
        password = str(request.form['input_passwd'])

        cursor.execute(
            "SELECT * FROM users WHERE uname = '{}'".format(username)
        )
        user = cursor.fetchone()

        if user is None:
            error = "Incorrect Username!"
        elif not check_password_hash(user[1], password):
            error = "Incorrect Password"

        if error is None:
            session.clear()
            session['pno'] = user[2]
            return redirect(url_for('bookticket'))

        flash(error)

    return render_template('login.html', error=error)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        _pno = request.form['input_pno']
        _fname = request.form['input_fname']
        _lname = request.form['input_lname']
        _dob = request.form['input_dob']
        _address = request.form['input_address']
        _phone = request.form['input_phone']
        _uname = request.form['input_uname']
        _passwd = request.form['input_password']
        
        cursor.execute(
            "SELECT * FROM users WHERE users.uname = '{}' or users.pno = '{}' or users.phone_no = '{}'".format(_uname, _pno, _phone)
        )
        if cursor.fetchone() is not None:
            error = 'User is already registered'
        
        if error is None:
            cursor.execute(
                "INSERT INTO users VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                    _uname,
                    generate_password_hash(_passwd),
                    _pno,
                    _fname,
                    _lname,
                    _dob,
                    _phone,
                    _address
                )
            )
            res = cursor.fetchall()
            conn.commit()
            return redirect (url_for('login'))
        
        flash(error)
    return render_template('signup.html', error = error)

@app.route("/bookticket", methods=['GET', 'POST'])
def bookticket():
    if request.method == 'GET':
        return render_template('app.html')
    else:
        _src = request.form['inputsrc']
        _dst = request.form['inputdest']
        # cursor.execute(
        #     "INSERT INTO users VALUES ('{}', '{}')".format(_src, _dst)
        # )
        # res = cursor.fetchall()
        # conn.commit()
        cursor.execute(
            "SELECT * FROM flight WHERE source = '{}' and destination = '{}'".format(_src, _dst)
        )
        flights = cursor.fetchall()
        return render_template('app.html', flights = flights)


@app.route("/payment", methods=['GET', 'POST'])
def payment():
    if request.method == 'GET':
        return render_template('payment.html')
    elif request.method == 'POST':
        pass

@app.route("/print", methods=['GET', 'POST'])
def print():
    if request.method == 'GET':
        return render_template('print.html')

# @app.before_request()
# def load_logged_in_user():
#     pno = session['pno']

#     if pno is None:
#         return redirect(url_for('login'))
#     else:
#         return redirect(url_for('bookticket'))

# route for login page
# @app.route('/login', methods=["GET","POST"])
# def login_page():
#     error = ''
#     try:
#         c, conn = connection()
#         if request.method == "POST":

#             data = c.execute("SELECT * FROM users WHERE username = (%s)", thwart(request.form['username']))
            
#             data = c.fetchone()[2]

#             if sha256_crypt.verify(request.form['password'], data):
#                 session['logged_in'] = True
#                 session['username'] = request.form['username']

#                 flash("You are now logged in")
#                 return redirect(url_for("dashboard"))

#             else:
#                 error = "Invalid credentials, try again."

#         gc.collect()

#     return render_template("login.html", error=error)

#     except Exception as e:
#         #flash(e)
#         error = "Invalid credentials, try again."
#         return render_template("login.html", error = error)


if __name__ == "__main__":
    #app.run(host = "0.0.0.0")
    app.run(debug = True)
