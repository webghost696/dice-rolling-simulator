#python project to get daily news headlines on the type of news you are interested in 
import requests
import json
query=input("What type of news are you interested in?:")
url=f"https://newsapi.org/v2/everything?q={query}&from=2023-02-27&sortBy=publishedAt&apiKey=035821fbe77449cbb94eef630ea6cf2e"
r=requests.get(url)
news=json.loads(r.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("---------------------------------")