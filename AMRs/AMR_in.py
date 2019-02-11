import numpy as np
import datetime
import time
import subprocess
import os
import re

# path = "C:\\Users\\Dennis\\Anaconda3\\Scripts"
# os.chdir(path)

## Must make sure path is right
def AMR_F(f1, f2):
    out = subprocess.check_output(["python", "smatch.py", "-f", f1, f2, "--pr", "--justinstance"])
    scores = re.findall(r"\d+\.\d+", str(out))
    return scores[-1]
    
def RDM_AMR(n):
    start = time.time()
    print("Start at {}".format(datetime.datetime.now()))
    path = "txt_"
    RDM2 = []
    for i in range(n):
        for j in range(n):
            if j > i:
                t1 = path+"{}.txt".format(i)
                t2 = path+"{}.txt".format(j)
                RDM2.append(float(AMR_F(t1, t2)))
        if i%50 == 0:
            np.save("scores\\50.npy", np.array(RDM2))
        if i%100 == 0:
            np.save("scores\\100.npy", np.array(RDM2))
            time2 = time.time()
            print("{} at min {}".format(i, ((time2-start)/60)))
    end = time.time()
    print("Done in {} min".format((end-start)/60))
    return RDM2
    
RDM = RDM_AMR(1253)
np.save("scores/RDM_AMR.npy", RDM)
print("Done")