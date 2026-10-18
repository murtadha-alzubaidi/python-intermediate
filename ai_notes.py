import os
import requests
import json
api_key=os.environ["GEMINI_API_KEY"]
url="https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-lite-latest:generateContent"
h={"x-goog-api-key": api_key}
question= input("Ask:")
body={"contents":[{"parts":[{"text": question}]}]}
try:
    r=requests.post(url,headers=h,json=body)
except requests.exceptions.ConnectionError:
    print("No internet connection")
    exit()
if r.status_code==200:
    data=r.json()
    answer= data["candidates"][0]["content"]["parts"][0]["text"]
    print(answer)
    try:
        with open("history.json","r")as f:
            history=json.load(f)
    except FileNotFoundError:
        history=[]
    history.append({"question":question,"answer":answer})
    with open("history.json","w")as f:
        json.dump(history,f,indent=4)
else:
    print(f"Request failed:{r.status_code}")
    print(r.text)