import json
with open("student.json","r")as f:
    data=json.load(f)
data["age"]=21
with open("student.json","w")as f:
    json.dump(data,f,indent=4)