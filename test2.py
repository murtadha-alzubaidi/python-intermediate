with open("fruits.txt","w")as f:
    f.write("apple\n")
    f.write("banana\n")
    f.write("orange\n")
with open("fruits.txt","a")as f:
    f.write("mango\n")
    f.write("pear\n")
with open("fruits.txt","r")as f:
    count=1
    total=0
    for line in f:
        print(f"{count}. {line.strip()}")
        count +=1
        total +=1
print(f"Total: {total} items")
try:
    with open("prices.txt","r")as f:
        print(f.read())
except FileNotFoundError:
    print("Prices not available")