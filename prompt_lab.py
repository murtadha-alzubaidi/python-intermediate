import os
import requests
api_key=os.environ["GEMINI_API_KEY"]
url="https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-lite-latest:generateContent"
headers={"x-goog-api-key": api_key}
def ask(prompt):
    body={"contents":[{"parts":[{"text": prompt}]}]}
    r=requests.post(url,headers=headers,json=body)
    if r.status_code==200:
        data = r.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return (f"Error {r.status_code}:{r.text}")
role="You are Python teacher for beginner university student. answer in short,simple sentences with a maximum of 60 words,and always include one small codw example."
print(ask(role+"Question:   What is for loop?"))