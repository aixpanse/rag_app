import requests


def search_websites(query: str):
    url = "http://127.0.0.1:8080/websites/search"
    data = {"query": query} 
    response = requests.post(url, json=data)
    res = response.json()
    print(res)
    return res.get("serialized", ""), res.get("retrieved_docs", "")

def create_order(payload):
    url = "http://127.0.0.1:8080/orders"
    response = requests.post(url, json=payload)
    res = response.json()
    print(res)
    return res

def create_message(payload):
    url = "http://127.0.0.1:8080/messages"
    response = requests.post(url, json=payload)
    res = response.json()
    print(res)
    return res

def list_orders():
    url = "http://127.0.0.1:8080/orders"
    response = requests.get(url)
    res = response.json()
    print(res)
    return res