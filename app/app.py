from discovery import register,get_ip_address
print(get_ip_address())

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/healthcheck')
def healthcheck():
    return 'OK'

service = register("app")
