
import subprocess
import os

# remove old log files
dir_name = os.getcwd()
test = os.listdir(dir_name)

for item in test:
    if item.endswith(".txt"):
        os.remove(os.path.join(dir_name, item))


# to do variable n from argv
subprocess.Popen(["python","producer.py","5","5000"])
subprocess.Popen(["python","otsu.py","5000","0"])
subprocess.Popen(["python","otsu.py","5001","1"])
subprocess.Popen(["python","otsu.py","5002","2"])
subprocess.Popen(["python","otsu.py","5003","3"])
subprocess.Popen(["python","otsu.py","5004","4"])
subprocess.Popen(["python","collector.py","5058","1"])
subprocess.Popen(["python","collector.py","5059","2"])
subprocess.Popen(["python","collector.py","5060","3"])
