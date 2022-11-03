from flask import Flask, request
from datetime import datetime
app = Flask('My First Application')

@app.route('/')

def index():
    return """

    <h1> Denyse Wepsites</h1>
    <p> my name is NIYONKURU</P>

    """

@app.route('/contact')

def contact_page():
    return " contact me at denyseniyonkuru22@gmail.com or 0783400316"

@app.route('/date')
def date_page():
    date = str(datetime.now())
    return f'To day is  {date}'

@app.route('/birthyear',methods=['POST','GET'])
def calc_birthyear():
    if request.method == 'POST':
        return f""" 
        <form ation='/birthyear' method='POST'> 
            <input type="number"  name="birthyear" placeholder="Birthyear eg 2020">
            <button type="submit">submit</button>
        </form>
        
        From  your submission  age is  {2022 - int(request.form.get('birthyear'))}"""
        #pass
    elif request.method == 'GET':
        return """

        <form ation='/birthyear' method='POST'> 
            <input type="number"  name="birthyear" placeholder="Birthyear eg 2020">
            <button type="submit">submit</button>
        </form>

        """

if __name__ == '__main__' :
    app.run()
