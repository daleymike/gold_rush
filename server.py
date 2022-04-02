from crypt import methods
from random import randint, random
from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'bruce banner was here'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['moves'] = 15
        session['activity'] = []
    return render_template("index.html")

@app.route('/process_gold', methods=['POST'])
def process_gold():
    session['moves'] -= 1
    if request.form['property'] == 'farm':
        random_gold = randint(10,20)
        session['gold'] += random_gold
        session['activity'].append(f"<div class='won'>Earned {random_gold} golds from the farm!</div> ")
    elif request.form['property'] == 'cave':
        random_gold = randint(5,10)
        session['gold'] += random_gold
        session['activity'].append(f"<div class='won'>Earned {random_gold} golds from the cave!</div>")

    elif request.form['property'] == 'house':
        random_gold = randint(2,5)
        session['gold'] += random_gold
        session['activity'].append(f"<div class='won'>Earned {random_gold} golds from the house!</div>")

    elif request.form['property'] == 'casino':
        earn_take = randint(0,1)
        random_gold = randint(0,50)
        if earn_take == 0:
            session['gold'] += random_gold
            session['activity'].append(f"<div class='won'>Earned {random_gold} golds from the casino!</div>")
        else:
            session['gold'] -= random_gold
            session['activity'].append(f"<div class='lost'>Yikes! You lost {random_gold} golds from the casino!</div>")
    return redirect("/")

@app.route('/restart')
def restart():
    session.clear()
    return redirect('/')




if __name__ == "__main__":
    app.run(debug = True)