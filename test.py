
import subprocess
import os
import sys
import math

n = int( sys.argv[1] )

# remove old log files
dir_name = os.getcwd()
test = os.listdir(dir_name)

for item in test:
    if item.endswith(".txt"):
        os.remove(os.path.join(dir_name, item))

subprocess.Popen(["python","producer.py","5000"])

for i in range(n):
        subprocess.Popen(["python","otsu.py","5000",str(i),"5058"])

for i in range ( int(math.ceil( n / 2 ) )):
        subprocess.Popen(["python","collector.py", "5058" , str(i) ,"6001"])

