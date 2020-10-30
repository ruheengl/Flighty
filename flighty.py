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

global i
i = 2

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
            session['uname'] = user[0]
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

@app.route("/logout", methods = ['GET'])
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route("/bookticket", methods=['GET', 'POST'])
def bookticket():
    if request.method == 'GET':
        return render_template('app.html')
    else:
        if request.form['submit_button'] == 'select_srcdest':
            _src = request.form['inputsrc']
            _dst = request.form['inputdest']
            cursor.execute(
                "SELECT * FROM flight WHERE source = '{}' and destination = '{}'".format(_src, _dst)
            )
            flights = cursor.fetchall()
            return render_template('app.html', flights = flights)
        else:
            fno = request.form['submit_button']
            return redirect(url_for('payment', flight = fno))

@app.route("/profile", methods=['GET', 'POST'])
def profile():
    if request.method == 'GET':
        cursor.execute("SELECT * FROM users WHERE uname = '{}'".format(session['uname']))
        res = cursor.fetchall()
        return render_template('users_view.html', result=res, content_type='application/json')
    else:
        return redirect(url_for('update'))

@app.route("/update", methods=['GET', 'POST'])
def update():
    # error = None
    if request.method == 'POST':
        _pno = request.form['input_pno']
        _fname = request.form['input_fname']
        _lname = request.form['input_lname']
        _dob = request.form['input_dob']
        _address = request.form['input_address']
        _phone = request.form['input_phone']
        # _uname = request.form['input_uname'] if not None
        _passwd = request.form['input_password']
        
        # cursor.execute(
        #     "SELECT * FROM users WHERE users.uname = '{}' or users.pno = '{}' or users.phone_no = '{}'".format(_uname, _pno, _phone)
        # )
        # if cursor.fetchone() is not None:
        #     error = 'User is already registered'
        
        # if error is None:
        if request.form.get('input_pno', None):
            cursor.execute(
            "UPDATE users SET pno='{}' where users.uname = '{}'".format(
                _pno,
                session['uname'],
            )
        )
        if request.form.get('input_fname', None):
            cursor.execute(
            "UPDATE users SET first_name='{}' where users.uname = '{}'".format(
                _fname,
                session['uname'],
            )
        )
        if request.form.get('input_lname', None):
            cursor.execute(
            "UPDATE users SET last_name='{}' where users.uname = '{}'".format(
                _lname,
                session['uname'],
            )
        )
        if request.form.get('input_dob', None):
            cursor.execute(
            "UPDATE users SET DOB='{}' where users.uname = '{}'".format(
                _dob,
                session['uname'],
            )
        )
        if request.form.get('input_address', None):
            cursor.execute(
            "UPDATE users SET address='{}' where users.uname = '{}'".format(
                _address,
                session['uname'],
            )
        )
        if request.form.get('input_phone', None):
            cursor.execute(
            "UPDATE users SET phone_no='{}' where users.uname = '{}'".format(
                _phone,
                session['uname'],
            )
        )
        if request.form.get('input_password', None):
            cursor.execute(
            "UPDATE users SET passwd='{}' where users.uname = '{}'".format(
                generate_password_hash(_passwd),
                session['uname'],
            )
        )
        res = cursor.fetchall()
        conn.commit()
        return redirect (url_for('profile'))
        
        # flash(error)
    return render_template('update.html')

@app.route("/payment", methods=['GET', 'POST'])
def payment():
    if request.method == 'GET' and not request.args.get('flight'):
        return redirect(url_for('bookticket'))
    elif request.args['flight']:
        flight_no = request.args['flight']
        username = session['uname']
        ticket_id = 'ticket'+str(i)
        i += 1
        price = 100
        status = 'yes'

        cursor.execute(
            "INSERT INTO ticket VALUES ('{}', '{}', '{}', '{}', '{}')".format(
                ticket_id,
                username,
                flight_no,
                status,
                price
            )
        )
        ins = cursor.fetchall()
        conn.commit()

        cursor.execute(
            "INSERT INTO booking VALUES ('{}', '{}')".format(ticket_id, flight_no)
        )
        ins = cursor.fetchall()
        conn.commit()

        # cursor.execute(
        #     """UPDATE TABLE flight SET count_ticket = count_ticket - 1 WHERE
        #      flight_id = '{}'""".format(flight_no)
        # )
        # update = cursor.fetchall()
        # conn.commit()

        cursor.execute(
            "INSERT INTO userMakesPayment VALUES ('{}', '{}')".format(username, ticket_id)
        )
        ins = cursor.fetchall()
        conn.commit()
        
        cursor.execute(
            """SELECT ticket_id, booking.flight_id, source, destination, first_name, last_name
                FROM booking, flight, users WHERE 
                ticket_id = '{}' AND
                booking.flight_id = flight.flight_id AND 
                users.uname = '{}'""".format(ticket_id, session['uname'])
        )
        payment = cursor.fetchone()
        return render_template('payment.html', payment = payment)

        

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


if __name__ == "__main__":
    #app.run(host = "0.0.0.0")
    app.run(debug = True)
