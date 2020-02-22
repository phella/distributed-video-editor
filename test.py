
import subprocess

subprocess.Popen(["python","producer.py","5","5000"])
subprocess.Popen(["python","otsu.py","5000","1"])
subprocess.Popen(["python","otsu.py","5001","2"])
subprocess.Popen(["python","otsu.py","5002","3"])
subprocess.Popen(["python","otsu.py","5003","4"])
subprocess.Popen(["python","otsu.py","5004","5"])
subprocess.Popen(["python","collector.py","5058","1"])
subprocess.Popen(["python","collector.py","5059","2"])
subprocess.Popen(["python","collector.py","5060","3"])
