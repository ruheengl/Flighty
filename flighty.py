from flask import Flask
from flaskext.mysql import MySQL
from flask import Flask, request, render_template, jsonify, redirect, url_for


mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'riley'
app.config['MYSQL_DATABASE_PASSWORD'] = 'riley'
app.config['MYSQL_DATABASE_DB'] = 'flight'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

# def view(table_name):
#     cursor.execute("select * from {}".format(table_name))
#     result = cursor.fetchall()
#     return result

@app.route("/",  methods=['GET', 'POST'])
def login():
    # cursor.execute("select * from script")
    # data = cursor.fetchall()

    # validate username and password here from database
    # ****************Here!****************************
    error = None
    if request.method == 'POST':
        if request.form['input_uname'] != 'admin' or request.form['input_passwd'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            # flash("You are successfuly logged in")
            return redirect(url_for('bookticket'))
    return render_template('login.html', error=error)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        _pno = request.form['input_pno']
        _fname = request.form['input_fname']
        _lname = request.form['input_lname']
        _dob = request.form['input_dob']
        # _email = request.form['input_email']
        _address = request.form['input_address']
        _phone = request.form['input_phone']
        _uname = request.form['input_uname']
        _passwd = request.form['input_password']
        cursor.execute("insert into user values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(_pno, _fname, _lname, _dob, _address, _phone, _uname, _passwd))
        res = cursor.fetchall()
        conn.commit()
        return render_template('login.html')

@app.route("/bookticket", methods=['GET', 'POST'])
def bookticket():
    if request.method == 'GET':
        return render_template('app.html')
    else:
        _src = request.form['input_src']
        _dst = request.form['input_dst']
        cursor.execute("insert into user values ('{}', '{}')".format(_src, _dst))
        res = cursor.fetchall()
        conn.commit()
        return render_template('payment.html')

@app.route("/payment", methods=['GET', 'POST'])
def payment():
    if request.method == 'GET':
        return render_template('payment.html')

@app.route("/print", methods=['GET', 'POST'])
def print():
    if request.method == 'GET':
        return render_template('print.html')

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
