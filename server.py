from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Servidor Flask funcionando!'

if __name__ == '__main__':
    app.run(debug=True, port=8080)