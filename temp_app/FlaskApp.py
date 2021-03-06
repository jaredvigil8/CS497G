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


@app.route('/enternewrequest')
def new_request():
	return render_template('request.html')


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
	message = "Before record insertion"
	if request.method == 'POST':
		try:
			nm = request.form['nm']
			addr = request.form['add']
			city = request.form['city']
			pin = request.form['pin']
			Type = request.form['Type']
			aid = request.form['aid']
			with sql.connect("database.db") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO allItems (name,addr,city,pin,Type,aid) VALUES (?,?,?,?,?,?)",(nm,addr,city,pin,Type,aid) 
)
				con.commit()
				message = "Record successfully added"
			with sql.connect("database.db") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO "+Type+" (name,addr,city,pin,Type,aid) VALUES (?,?,?,?,?,?)",(nm,addr,city,pin,Type,aid))
				con.commit()
				message = "Record successfully added into "+Type
		except:
			con.rollback()
			message = "Error in insert operation"

		finally:
			return render_template("result.html", msg = message)
			con.close()

@app.route('/listdonations')
def listdonations():
        con = sql.connect("database.db")	
	con.row_factory = sql.Row
	
	cur = con.cursor()
	cur.execute("select * from allItems WHERE aid = 'donation'")

	rows = cur.fetchall()
	return render_template('list.html', rows = rows)

@app.route('/listrequests')
def listrequests():
        con = sql.connect("database.db")	
	con.row_factory = sql.Row
	
	cur = con.cursor()
	cur.execute("select * from allItems WHERE aid = 'request'")

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

@app.route('/Contact')
def Contact():
    return render_template('contact.html')

@app.route('/Signup')
def Signup():
    return render_template('signup.html')
@app.route('/showFood')
def showFood(): 

	aid = request.args.get('aid', None)
	con = sql.connect("database.db")	
	con.row_factory = sql.Row
	
	cur = con.cursor()
	cur.execute("select * from food WHERE aid = '"+aid+"'")

	rows = cur.fetchall()
	return render_template('list.html', rows = rows)

@app.route('/showHygiene')
def showHygiene():

	aid = request.args.get('aid', None)
	con = sql.connect("database.db")	
	con.row_factory = sql.Row
	
	cur = con.cursor()
	cur.execute("select * from hygiene WHERE aid = '"+aid+"'")

	rows = cur.fetchall()
	return render_template('list.html', rows = rows)

@app.route('/showOddjobs')
def showOddjobs():
	aid = request.args.get('aid', None)
	con = sql.connect("database.db")	
	con.row_factory = sql.Row
	
	cur = con.cursor()
	cur.execute("select * from jobs WHERE aid = '"+aid+"'")

	rows = cur.fetchall()
	return render_template('list.html', rows = rows)
@app.route('/showClothes')
def showClothes():
	aid = request.args.get('aid', None)
	con = sql.connect("database.db")	
	con.row_factory = sql.Row
	
	cur = con.cursor()
	cur.execute("select * from clothes WHERE aid = '"+aid+"'")

	rows = cur.fetchall()
	return render_template('list.html', rows = rows)

@app.route('/showShelter')
def showShelter():
	aid = request.args.get('aid', None)
	con = sql.connect("database.db")	
	con.row_factory = sql.Row
	
	cur = con.cursor()
	cur.execute("select * from shelter WHERE aid = '"+aid+"'")

	rows = cur.fetchall()
	return render_template('list.html', rows = rows)

@app.route('/showTransportation')
def showTransportation():
	aid = request.args.get('aid', None)
	con = sql.connect("database.db")	
	con.row_factory = sql.Row
	
	cur = con.cursor()
	cur.execute("select * from transportation WHERE aid = '"+aid+"'")

	rows = cur.fetchall()
	return render_template('list.html', rows = rows)

if __name__ == "__main__":
    app.run(debug = True)
