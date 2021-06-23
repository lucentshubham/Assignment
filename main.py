from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import RequestHeaderFieldsTooLarge
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/assignment'
app.config['SQLALCHEMY_BINDS'] = {
        'postgresql': 'postgresql://Shubham:Shubham123@@localhost:5432/assignment'
}
db = SQLAlchemy(app)
class MySql(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(10), nullable=False)
   
class PostgreSql(db.Model):
    __bind_key__ = 'postgresql'
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(10), nullable=False)

@app.route('/MySql')
def MySql():
    return render_template('mysql.html')
@app.route("/postgresql")
def PosrgreSql():
    return render_template('postgresql.html')

#app.run(debug=True)