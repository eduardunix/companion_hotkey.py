import keyboard
import requests

def fetch_data_from_api_1():
    url = "http://127.0.0.1:8000/api/location/2/0/6/press"
    response = requests.post(url)
    if response.status_code == 200:
        print("Data from API 1 fetched successfully")
        data = response.json()
    else:
        print(f"Status code: {response.status_code}")

def fetch_data_from_api_2():
    url = "http://127.0.0.1:8000/api/location/2/1/6/press"
    response = requests.post(url)
    if response.status_code == 200:
        print("Data from API 2 fetched successfully")
        data = response.json()
    else:
        print(f"Status code: {response.status_code}")

def fetch_data_from_api_3():
    url = "http://127.0.0.1:8000/api/location/2/2/6/press"
    response = requests.post(url)
    if response.status_code == 200:
        print("Data from API 2 fetched successfully")
        data = response.json()
    else:
        print(f"Status code: {response.status_code}")


def fetch_data_from_api_4():
    url = "http://127.0.0.1:8000/api/location/2/3/6/press"
    response = requests.post(url)
    if response.status_code == 200:
        print("Data from API 2 fetched successfully")
        data = response.json()
    else:
        print(f"Status code: {response.status_code}")

def on_key_event(event):
    if event.name == 'f13':
        fetch_data_from_api_1()
    elif event.name == 'f14':
        fetch_data_from_api_2()
    elif event.name == 'f15':
        fetch_data_from_api_3()
    elif event.name == 'f16':
        fetch_data_from_api_4()        

keyboard.on_press(on_key_event)

keyboard.wait('esc')
