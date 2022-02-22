from requests import Request, Session
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {
    'slug': 'bitcoin,ethereum'
}

key = 'f47e78f7-c792-4155-8639-9f142c7556f1'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': key,
}

session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)
data = json.loads(response.text)

data = data["data"]
for i in data:
    id = next(iter( data.items() ))
    id=id[0]
    data = data[str(id)]
    print(data)