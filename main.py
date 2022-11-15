import os
import json

yourpath = 'labels'

for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:
        print(os.path.join(root, name))
        f = open(os.path.join(root,name))
        data = json.load(f)
        result = str(data)
        print("The frame of yes:",result.count(" 1"))
        print("Total frame:", result.count(":"))
        f.close
    #for name in dirs:
       #print(os.path.join(root, name))
