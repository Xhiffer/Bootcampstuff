from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/your.number.<numero>', methods=['GET', 'POST'])
def serveur(numero) :
    return jsonify({"numero":int(numero)**2})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug=True)