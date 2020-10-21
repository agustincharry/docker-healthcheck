from flask import Flask

app = Flask(__name__)
http_status = 200

@app.route('/')
def index():
    return 'App status: ' + str(http_status), http_status

@app.route('/down')
def down():
    global http_status
    http_status = 500
    return 'Turning off...'

@app.route('/up')
def up():
    global http_status
    http_status = 200
    return 'Turning on!...'

if __name__ == '__main__':
    app.run(host='0.0.0.0')