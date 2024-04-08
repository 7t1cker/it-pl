from flask import Flask

app = Flask(__name__)

@app.route('/s')
def hello_world():
    return 'эй эй эй'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)