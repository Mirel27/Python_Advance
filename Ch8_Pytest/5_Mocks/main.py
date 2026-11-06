import requests

def api_call(url):
    response = requests.get(url)
    data = response.json()
    return {"data": data}