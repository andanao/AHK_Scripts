# %%
from translate import Translator

to_lang = 'en'
key1 = '25b27cf625b14347a856c4c75cf34697'
key2 = '8f77caba0e06480bb2170e1c8415baa1'
tw = '是在'

trans = Translator(provider='microsoft', to_lang='zh',secret_access_key=key1)
trans.translate(tw)
# %%
import requests, uuid, json

# Add your subscription key and endpoint
subscription_key = key
endpoint = "https://api.cognitive.microsofttranslator.com"

# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.
# location = "YOUR_RESOURCE_LOCATION"
location = "eastus"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['zh-CH', 'es']
}
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text': 'testing!'
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
# %%
