class TodoItem:
	def __init__(self, id, text):
		self.id = id
		self.text = text
		self.done = False

	def __str__(self):
		done = 'done' if self.done else 'not done'
		return "[Item %d] %s is %s" % (self.id, self.text, done)

	def asdict(self):
		return {'id': self.id, 'text': self.text, 'done': self.done }
