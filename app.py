from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'API is Live!'

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')

