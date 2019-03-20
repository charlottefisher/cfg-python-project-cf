import requests

id = "84600bca7507293656495e8972aec659"
payload = {'q':'Sheffield, UK', 'units':'metric', 'appid':id}

def query_weather(payload):
    endpoint = "http://api.openweathermap.org/data/2.5/weather"
    response = requests.get(endpoint, params=payload)

    return response

response = query_weather(payload)

print(response)
print(response.text)

def jsonify(response):
    json_response = response.json()
    return json_response


json_response = jsonify(response)
print("\n")
#print(json_response)
# Displays the data in a nicer way
import pprint
#pprint.pprint(json_response)


print("The temperature outside is:", json_response['main']['temp'], "degrees celcius")

temp = json_response['main']['temp']

if temp < 10:
    print("So start boiler")
else:
    print("So keep boiler off")
