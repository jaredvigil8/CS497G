from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

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
    app.run()
