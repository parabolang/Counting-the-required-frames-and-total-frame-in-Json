import os
import json
import numpy as np

yourpath = 'labels'
count=np.zeros((20,), dtype=int)
print(count[0])
for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:
        print(os.path.join(root, name))
        f = open(os.path.join(root,name))
        data = json.load(f)
        result = str(data)
        print("The frame of yes:",result.count(" 1"))
        print("Total frame:", result.count(":"))
        i=os.path.join(root, name)
        print(i[len(i)-6])
        print(type(i[2]))
        for iter_var in range( len( count ) ):
            if i[len(i)-6] == str(iter_var) and  i[len(i)-7] != str(1):
                count[iter_var]=count[iter_var]+result.count(" 1")
            elif i[len(i)-6] == str(iter_var) and i[len(i)-7] == str(1):
                count[iter_var]=count[iter_var]+result.count(" 1")
        f.close
    #for name in dirs:
       #print(os.path.join(root, name))
print (count)

