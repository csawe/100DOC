import requests

drinks_url = "http://127.0.0.1:5000/drinks"

data_payload = {"name": "Krest", "description": "A taste of Africa"}

def get_drinks():
    response = requests.get(drinks_url)
    print(response.json())
    
def get_drink(id):
    url = drinks_url+ f"/{id}"
    response = requests.get(url)
    print(response.json())
    
def add_drink():
    response = requests.post(drinks_url, json=data_payload)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Failed to post data")
        
# get_drink(5)
# get_drinks()
add_drink()