import os
import requests
api_key=os.environ["GEMINI_API_KEY"]
url="https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-lite-latest:generateContent"
headers={"x-goog-api-key": api_key}
question = input("Ask:")
body={"contents":[{"parts":[{"text": question}]}]}
r=requests.post(url,headers=headers,json=body)
if r.status_code==200:
    data = r.json()
    answer = data["candidates"][0]["content"]["parts"][0]["text"]
    print(answer)
else:
    print(f"Request failed: {r.status_code}")
    print(r.text)