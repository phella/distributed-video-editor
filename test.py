
import subprocess
import os

# remove old log files
dir_name = os.getcwd()
test = os.listdir(dir_name)

for item in test:
    if item.endswith(".txt"):
        os.remove(os.path.join(dir_name, item))


# to do variable n from argv
subprocess.Popen(["python","producer.py","1","5000"])
subprocess.Popen(["python","otsu.py","5000","0","5058"])
subprocess.Popen(["python","collector.py","5058","1","6001"])
subprocess.Popen(["python","contour.py","6001","1","4000"])     
subprocess.Popen(["python","contour.py","6002","1","4000"])
subprocess.Popen(["python","collector2.py","4000"])
