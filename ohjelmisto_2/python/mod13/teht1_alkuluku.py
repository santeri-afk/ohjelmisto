from flask import Flask, request


app = Flask(__name__)
@app.route('/alkuluku')
def alkuluku():
    args = request.args
    luku = int(args.get("luku1", 4))
    if alkuluku luku % luku == 0:
        print("tämä ei ole alkuluku")
        a = True

    else:
        a = False
    
    

    vastaus = {
        "number" : luku,
        "isprime" : a
    }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)