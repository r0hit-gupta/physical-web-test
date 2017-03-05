import sys

# A class to handle the queue and its functions
class Queue(object):

	def __init__(self):
		self.queue = []

	# Enqueue element x into the end of the queue
	def put(self, element):
		self.queue.append(element)

	# Dequeue the element at the front of the queue.
	def pop(self):
		self.queue.pop(0)

	# Print the element at the front of the queue.
	def peek(self):
		print(self.queue[0])

# Selection of the input function to be used based on the python version.
if sys.version_info.major < 3:
	inputs  = raw_input
else:
	inputs = input

# input the number of total actions to be performed
total_actions = int(inputs())

# new object of class Queue
queue = Queue()

for x in range(total_actions):
	
	# breaks the input into a list
	inp = [int(n) for n in inputs().split(' ')]
	
	# perform respective actions as given in the problem statement
	if(inp[0] == 1):
		queue.put(inp[1])
	
	elif(inp[0] == 2):
		queue.pop()
	
	elif(inp[0] == 3):
		queue.peek()
	