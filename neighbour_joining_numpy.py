import re
import numpy as np
coo = np.array([])
row = 0
with open (r"PentaAla.pdb", "r") as f:
    for line in f.readlines():
        m = re.search ("^ATOM *[0-9]* *([NCAOHBT123]*).*      ([ -][0-9]*[.][0-9]*) *([ -][0-9]*[.][0-9]*) *([ -][0-9]*[.][0-9]*)", line)
        if m:
            coo = np.append(coo, list(m.groups()))
            row += 1
coo = coo.reshape(row, 4)
print ("Atom\t\tNeighbour\t\tDistance")
for i in range (row):
    for j in range (i+1, row):
        dist = ((float(coo[i,1]) - float(coo[j,1]))**2 + (float(coo[i,2]) - float(coo[j,2]))**2 + (float(coo[i,3]) - float(coo[j,3]))**2)**0.5
        if dist <= 13:
            print (f"{coo[i,0]}({i+1})\t\t{coo[j,0]}({j+1})\t\t{dist}")
