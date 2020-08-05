import time
from subprocess import call

print("runpy basla")
time.sleep(5)
call(["python", "ModulTest.py"])
print("runpy end")