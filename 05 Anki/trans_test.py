# %%
import requests, uuid, json

class Translator():
    '''
    Using Microsoft translation API to translate
    Key - API Key
    src - Source language (default zh-Hans)
    dest - destination language (default en)
    '''
    def __init__(self,key='',src='zh-Hans',dest='en'):
        if key =='':
            print('no key defined!')
        
        self.subscription_key = key
        endpoint = "https://api.cognitive.microsofttranslator.com"
        location = "eastus"
        path = '/translate'

        self.constructed_url = endpoint + path
        self.params = {
            'api-version': '3.0',
            'from': src,
            'to': dest
        }
        
        self.headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }
        # You can pass more than one object in body.
        self.body = [
            {'text': 'testing!'}
        ]

    def _make_request(self,body):
        request = requests.post(
            self.constructed_url, 
            params=self.params, 
            headers=self.headers, 
            json=body)
        response = request.json()
        # print(json.dumps(response, sort_keys=True, ensure_ascii=False,indent=4, separators=(',', ': ')))
        return response

    def translate(self, word):
        '''
        pass word as string or as list
        '''
        body = []
        if isinstance(word,str):
            body.append({'text':word})
        if isinstance(word,list):
            for i in word:
                body.append({'text':i})

        response =  self._make_request(body)
        out = []
        for i in response:
            out.append(i['translations'][0]['text'])
        return out

if __name__ == "__main__":
    to_lang = 'en'
    key1 = '25b27cf625b14347a856c4c75cf34697'
    key2 = '8f77caba0e06480bb2170e1c8415baa1'
    tw = '是在'
    tl = ['的确','可以吗？']
    trans = Translator(key=key1)

    # trans._make_request(body)

    print(trans.translate(tw))
    print(trans.translate(tl))

    

