import json
books=[{"title":"meow","pages":77},
       {"title":"cats","pages":300}]
with open("books.json","w")as f:
    json.dump(books,f,indent=4)
with open("books.json","r")as f:
    data=json.load(f)
for book in data:
    print(f"{book['title']}:{book['pages']} pages")
try:
    with open("settings.json","r")as f:
        settings=json.load(f)
except FileNotFoundError:
    print("No settings found")