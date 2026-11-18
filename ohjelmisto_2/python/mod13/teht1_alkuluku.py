from flask import Flask


app = Flask(__name__)

def alkuluku(luku):
    for i in range(2, luku):
        if luku % i == 0:
            return False

       
    return True
    
@app.route('/alkuluku/<int:luku>')
def tarkistus(luku):
    vastaus = alkuluku(luku)
    tulostus = {
        "number" : luku,
        "isprime" : vastaus
    }

    return tulostus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
