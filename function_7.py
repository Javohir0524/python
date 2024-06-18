message = "a"

def greet(name):
	global message
	message = "b"

greet("Javohir")
print(message)
