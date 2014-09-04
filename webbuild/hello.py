from flask import Flask
from flask import render_template
from flask import abort, redirect, url_for
app = Flask(__name__)
@app.route('/cmplst/')
def indexpage():
    return render_template('cmplst.html')

@app.route('/cmplst/<name>')
def newpage(name):
    return redirect(url_for('static', filename = name))
if __name__ == '__main__':
    app.run()
