import subprocess
import os
import sys

n = int( sys.argv[1] )

''' unccomment when using 2 laptops

# remove old log files
dir_name = os.getcwd()
test = os.listdir(dir_name)

for item in test:
    if item.endswith(".txt"):
        os.remove(os.path.join(dir_name, item))

'''
for i in range(n):
	subprocess.Popen(["python","contour.py","6001",str(i),"4000"])

subprocess.Popen(["python","collector2.py","4000"])