from flask_socketio import SocketIO, Namespace

class SomeActions(Namespace):
	def on_connect(self):
		print('OK!')

class MyWebSocket(SocketIO):
	def __init__(self, app, **kwargs):
		super().__init__(app, **kwargs)
		self.on_namespace(SomeActions())


