from ws.app import MyWebSocket
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socket = MyWebSocket(app)

@app.route('/')
def index():
	return render_template('main.html')

if __name__ == '__main__':
	socket.run(app, allow_unsafe_werkzeug=True)