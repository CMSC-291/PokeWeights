import requests
import json
import matplotlib.pyplot as plt

poke_url = "https://pokeapi.co/api/v2/pokemon/"

poke_json = requests.get(poke_url).text
pokemon = json.loads(poke_json)

# print((pokemon['results']))

ids = []
weights = []
for result in pokemon['results']:
    res_json = requests.get(result['url']).json()
    ids.append(res_json['id'])
    weights.append(res_json['weight'])
    print(result['name'], "Weight:", res_json['weight'])

plt.plot(ids, weights, 'rd')
plt.title("ID vs Weight")
plt.xlabel("IDs")
plt.ylabel("Weights")
plt.show()
