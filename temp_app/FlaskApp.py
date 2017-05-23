from flask import Flask, render_template, request, flash, url_for, redirect
import sqlite3 as sql


app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/index')
def home():
	return render_template('index.html')

@app.route('/enternew')
def new_student():
	return render_template('student.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
	if request.method == 'POST':
		try:
			nm = request.form['nm']
			addr = request.form['add']
			city = request.form['city']
			pin = request.form['pin']

			with sql.connect("database.db") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO items (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) 
)
				con.commit()
				msg = "Record successfully added"
		except:
			con.rollback()
			msg = "Error in insert operation"

		finally:
			return render_template("result.html", msg = msg)
			con.close()

@app.route('/list')
def list():
        con = sql.connect("database.db")	
	con.row_factory = sql.Row
	
	cur = con.cursor()
	cur.execute("select * from items")

	rows = cur.fetchall()
	return render_template('list.html', rows = rows)

	
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
    app.run(debug = True)
