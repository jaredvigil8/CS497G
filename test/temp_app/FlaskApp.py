from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
@app.route("/")
def main():
    return render_template('index.html')

db = SQLAlchemy(app)
class users(db.Model):
    id = db.Column('user_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

db.create_all()
@app.route('/index')
def home():
	return render_template('index.html')

@app.route('/show_all')
def show_all():
        return render_template('show_all.html', users = users.query.all())

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields', 'error')
        else:
            user = users(request.form['name'], request.form['city'], request.form['addr'], request.form['pin'])
            db.session.add(user)
            db.session.commit()
            flash('Record was successfuly added')
            return redirect(url_for('show_all'))
    return render_template('new.html')

@app.route('/Donate')
def Donate():
    return render_template('donate.html')

@app.route('/Receive')
def Receive():
    return render_template('receive.html')

@app.route('/Tutorial')
def Tutorial():
    return render_template('tutorial.html')

@app.route('/Signup')
def Signup():
    return render_template('signup.html')
@app.route('/showFood')
def showFood():
    return render_template('searchResults.html')

@app.route('/showHygiene')
def showHygiene():
    return render_template('searchResults.html')

@app.route('/showOddjobs')
def showOddjobs():
    return render_template('searchResults.html')

@app.route('/showClothes')
def showClothes():
    return render_template('searchResults.html')

@app.route('/showShelter')
def showShelter():
    return render_template('searchResults.html')

@app.route('/showTransportation')
def showTransportation():
    return render_template('searchResults.html')

if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)
