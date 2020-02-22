import inspect

def log(str):
	frame = inspect.stack()[1]
	module = inspect.getmodule(frame[0])
	filename = module.__file__
	filename = filename[0:-3]
	filename += ".log.txt"
	f= open(filename,"a+")
	f.write(str)
	