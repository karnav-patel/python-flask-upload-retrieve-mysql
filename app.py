from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'karnavpatel'
app.config['MYSQL_DB'] = 'karnav'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO persons(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        #return 'success'
    curOne = mysql.connection.cursor()
    curOne.execute("SELECT FirstName FROM persons")
    rows = curOne.fetchall()
    return render_template('index.html', rows=rows)


if __name__ == '__main__':
    app.run()