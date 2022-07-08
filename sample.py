command = "ls -lrtfdd"
import os
try:
    os.system(command11)
except Exception as e:
    print("Exception : %e while start ssh on DPU" % e)
