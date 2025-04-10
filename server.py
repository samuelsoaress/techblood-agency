from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return  render_template('index.html')#'Servidor Flask funcionando!'

@app.route('/social_media')
def index():
    return  render_template('social_media.html')#'Servidor Flask funcionando!'

@app.route('/branding')
def index():
    return  render_template('branding.html')#'Servidor Flask funcionando!'

@app.route('/')
def index():
    return  render_template('web_services.html')#'Servidor Flask funcionando!'

if __name__ == '__main__':
    app.run(debug=True, port=8080)