import time
import requests
import json



API = "https://jsonplaceholder.typicode.com/todos/1"
def runner():
    print("This is our scheduled task runnif")
    data = requests.get(API)
    print(json.loads(data.content))




while True:
    time.sleep(2)
    runner()