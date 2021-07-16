from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'database-j.cepbobatridn.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'Jaya1234'
app.config['MYSQL_DB'] = 'MyDb'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        Name = details['Name']
        Number = details['Number']
        Age = details['Age']
        Location = details['Location']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Myusers(Name,Number,Age,Location) VALUES (%s, %s, %s, %s)", (Name,Number,Age,Location))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

@app.route('/users')
def users():
    cur =mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Myusers")
    
    if resultValue > 0:
        usersDetails = cur.fetchall()
        return render_template('users.html',usersDetails=usersDetails)
if __name__ == '__main__':
  app.run(host="0.0.0.0",port=80)
