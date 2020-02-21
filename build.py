import os

const base1 = 5557
const n = 5 
os.system('cmd /c "python producer.py 5 5557"') # n and base socket
for i in range(n):
	os.system('cmd /c "python otsu.py ' + str(base1+i) +'"')
