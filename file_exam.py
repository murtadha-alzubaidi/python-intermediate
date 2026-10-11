try:
    with open("missing.text","r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")