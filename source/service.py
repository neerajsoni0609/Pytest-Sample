import requests

database = {
    1 : "Neeraj",
    2 : "Poonam",
    3 : "Vinayak"
}

def get_user_from_db(user_id):
    return database.get(user_id)

def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    if response.status_code == 200:
        return response.json()
    
    raise requests.HTTPError