import csv 
import requests

url = 'http://api.coincap.io/v2/assets'

headers = {
    'Accept' : 'application/json',                      #Please give me the response in JSON format
    'Content-type' : 'application/json'                 # and by the way, I'm sending you data in JSON format too."
}

response = requests.request("GET",url,headers=headers,data={})
myjson = response.json()

#print(myjson)

#print("Data : " ,myjson['data']['id'])

ourdata = []
for x in myjson['data'] :
    listing = [x['id'],x['symbol'],x['name'],x['priceUsd']]
    ourdata.append(listing)

#print(ourdata)

csvheader = ['id','symbol','name','priceUSD']                           #creating a header section for the csv file we are going to create
with open('crypto.csv','w',encoding = 'UTF8',newline='') as f:
#with statement is used to avoid errors while writing
#UTF8 which stands for "Unicode Transformation Format - 8-bit," is a character encoding standard used to represent text in computers. 
    #it is a better practice to specify it when you are reading a data from external source

    outputCSV = csv.writer(f)
    outputCSV.writerow(csvheader)                  #frist writes csvheader as the frist line in the output file
    outputCSV.writerows(ourdata)                    #then writes the data that we have extracted 

print("done")