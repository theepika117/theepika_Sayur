import requests

url = 'http://api.coincap.io/v2/assets'

data = requests.get(url)

if data.status_code == 200 :
    jsonData = data.json()
    print(jsonData)

else :
    print("Error : ",data.status_code)