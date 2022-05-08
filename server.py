from operator import methodcaller
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)    
app.secret_key = 'asNTd@O#PH5d2sc'

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    print(request.form)
    print(request.form['name'])
    print(request.form['location'])
    print(request.form['favLan'])
    print(request.form['comments'])

    session['name']= request.form['name']
    session['location']= request.form['location']
    session['favLan']= request.form['favLan']
    session['comments']= request.form['comments']

    return redirect('/results')

@app.route('/results')
def results():
    print(session['name'])
    return render_template('show.html')




if __name__=="__main__":   
    app.run(debug=True)  