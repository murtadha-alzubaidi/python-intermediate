import json
tasks=[{"title":"Study JSON","done":True},
       {"title":"Push to Github","done":False}]
with open("tasks.json","w")as f:
    json.dump(tasks,f,indent=4)
with open("tasks.json","r")as f:
    data=json.load(f)
for task in data:
    print(f"{task['title']}-{task['done']}")
try:
    with open("config.json","r")as f:
        config=json.load(f)
except FileNotFoundError:
    print("Config file not found")