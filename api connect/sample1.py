import requests

url = 'http://api-testnet.bybit.com'

data = requests.get(url)

if data.status_code == 200 :
    jsonData = data.json()
    print(jsonData)

else :
    print("Error : ",data.status_code)