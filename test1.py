with open("tasks.txt","w") as f:
    f.write("Study Python\n")
    f.write("Learning AI\n")
    f.write("API\n")
with open("tasks.txt","a") as f:
    f.write("OpenAI\n")
with open("tasks.txt","r") as f:
    count=1
    for line in f:
        print(f"{count}. {line.strip()}")
        count +=1
try:
    with open("done.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("No completed tasks yet")