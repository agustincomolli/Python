import requests, json

for i in range(10):
    result = requests.get("https://randomuser.me/api/")
    user = result.json()
    
    for person in user["results"]:
        name = f"{person['name']['first']} {person['name']['last']}"
        image = person["picture"]["medium"]
    
    picture = requests.get(image)
    with open(f"./images/{name}.jpg", mode="wb") as file:
        file.write(picture.content)